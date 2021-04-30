import fnmatch
import numpy as np

import scipy.interpolate

import GPy
import emcee


from ps_eor import psutil

def c_nu_from_ps21_fct(ps3d_fct, freqs, uv_bins, delta_kpar=0.05):
    ''' Return frequency-frequency covariance for the given baselines bins and frequency 
        given the spherically averaged power-spectra P(k) (and not delta(k)). 
        Assume isotropie of the signal, which is true to some extend for the 21-cm signal.
        
        See https://arxiv.org/abs/astro-ph/0605546'''

    z = psutil.freq_to_z(freqs.mean())
    
    delay = psutil.get_delay(freqs, half=False)
    k_par = psutil.delay_to_k(delay, z)
    k_par = np.arange(k_par.min(), k_par.max() + delta_kpar, delta_kpar)
    
    uu = np.array(uv_bins).mean(axis=1)
    ll = 2 * np.pi * uu
    k_per = psutil.l_to_k(ll, z)
    
    k_pers, k_pars = np.meshgrid(k_per, k_par)
    lls, delays = np.meshgrid(ll, delay)
    
    ks = np.sqrt(k_pers ** 2 + k_pars ** 2)

    delta_f = freqs[:len(freqs) // 2] - freqs[0]
    delta_r = delta_f * psutil.freqency_to_comoving_distance(z)

    c_nu_nu = (ps3d_fct(ks)[:, :, None] * np.cos(delta_r[None, None, :] * k_pars[:, :, None])).sum(axis=0).T 
    c_nu_nu = c_nu_nu / c_nu_nu.max()

    return c_nu_nu.T
    

def c_nu_from_ps21(k_mean, ps3d, freqs, uv_bins, delta_kpar=0.05):
    ps_fct = lambda k: 1 / k ** 3 * scipy.interpolate.interp1d(k_mean, ps3d, 
                                                               bounds_error=False, 
                                                               kind='quadratic', 
                                                               fill_value='extrapolate')(k)
    
    return np.clip(c_nu_from_ps21_fct(ps_fct, freqs, uv_bins, delta_kpar=0.05), 1e-20, 1e20)



class MLKern(GPy.kern.Kern):
    ''' GPy compatible kernel generated from ML. Asbtract class. See VAEKern for the VAE implementation '''
    
    def __init__(self, ml_decoder, latent_dim, freqs, uv_bins, name='ml_kern', param_values=[]):
        from paramz.transformations import Logexp

        GPy.kern.Kern.__init__(self, 1, 0, name)
        self.ml_decoder = ml_decoder
        self.latent_dim = latent_dim
        self.uv_bins = uv_bins
        self.freqs = freqs
        self.params = [GPy.core.parameterization.Param(f'x{i + 1}', 0, ) for i in range(self.latent_dim)]
        self.params.append(GPy.core.parameterization.Param('variance', 1, Logexp()))
        self.link_parameters(*self.params)
        for i, pvalue in zip(range(self.latent_dim), param_values):
            setattr(self, f'x{i + 1}', pvalue)
        self.params_call = []
        
        self.dnu = np.diff(self.freqs * 1e-6).mean()
        
    def copy(self):
        c = self.__class__(self.ml_decoder, self.latent_dim, self.freqs, self.uv_bins, name=self.name)
        [c.unlink_parameter(p) for p in c.params]
        c.params = [k.copy() for k in self.params]
        c.link_parameters(*c.params)
        c._connect_parameters()
        c._connect_fixes()
        c._notify_parent_change()

        return c
    
    def get_norm_cov_1d(self, params):
        raise NotImplementedError()
    
    def K(self, X, X2=None):
        norm_cov_1d = self.get_norm_cov_1d(np.array(self.params[:-1]).T)
        r_1d = self.dnu * np.arange(norm_cov_1d.shape[1])

        Xsq = np.sum(np.square(X),1)
        r2 = -2. * np.dot(X, X.T) + (Xsq[:,None] + Xsq[None,:])
        r2[np.diag_indices(X.shape[0])] = 0.
        r2 = np.clip(r2, 0, np.inf)
        r = np.sqrt(r2)

        cov = scipy.interpolate.interp1d(r_1d, norm_cov_1d, kind='quadratic', axis=1, 
                                         bounds_error=False, fill_value=0)(r)
        
        return self.params[-1][0] * cov


class VAEKern(MLKern):
    
    def __init__(self, decoder, latent_dim, freqs, uv_bins, name='vae_kern', param_values=[]):
        MLKern.__init__(self, decoder, latent_dim, freqs, uv_bins, name=name, param_values=param_values)
    
    def get_norm_cov_1d(self, params):
        ps3d = self.ml_decoder.predict(params).squeeze()
        k_mean = np.array([0.06159647, 0.0906642 , 0.13162709, 0.18845897, 0.27278156,
                           0.39485285, 0.5716114 , 0.82662547, 1.15585453, 1.68722512])
        
        ps3d = k_mean ** 1 * ps3d
        return c_nu_from_ps21(k_mean, ps3d, self.freqs, self.uv_bins, delta_kpar=0.05)


class PCAKern(MLKern):
    
    def __init__(self, pca, latent_dim, freqs, uv_bins, name='pca_kern', param_values=[]):
        MLKern.__init__(self, pca, latent_dim, freqs, uv_bins, name=name, param_values=param_values)
        
    def get_norm_cov_1d(self, params):
        return self.ml_decoder.inverse_transform(params).reshape(4, 31)

    
class PSKern(GPy.kern.Kern):
    
    def __init__(self, k_mean, freqs, uv_bins, name='ps_kern', param_values=[]):
        from paramz.transformations import Logexp

        GPy.kern.Kern.__init__(self, 1, 0, name)
        self.uv_bins = uv_bins
        self.freqs = freqs
        self.k_mean = k_mean
        self.params = [GPy.core.parameterization.Param(f'x{i + 1}', 0, Logexp()) for i in range(len(self.k_mean))]
        self.link_parameters(*self.params)
        for i, pvalue in zip(range(len(self.k_mean)), param_values):
            setattr(self, f'x{i + 1}', pvalue)
        self.params_call = []
        
        self.dnu = np.diff(self.freqs * 1e-6).mean()
        
    def copy(self):
        c = self.__class__(self.k_mean, self.freqs, self.uv_bins, name=self.name)
        [c.unlink_parameter(p) for p in c.params]
        c.params = self.params.copy()
        c.link_parameters(*c.params)
        
        return c
    
    def get_norm_cov_1d(self, params):
        return c_nu_from_ps21(self.k_mean, params, self.freqs, self.uv_bins, delta_kpar=0.05) 
    
    def K(self, X, X2=None):
        norm_cov_1d = self.get_norm_cov_1d(np.array(self.params).squeeze())
        r_1d = self.dnu * np.arange(norm_cov_1d.shape[1])

        Xsq = np.sum(np.square(X),1)
        r2 = -2. * np.dot(X, X.T) + (Xsq[:,None] + Xsq[None,:])
        r2[np.diag_indices(X.shape[0])] = 0.
        r2 = np.clip(r2, 0, np.inf)
        r = np.sqrt(r2)

        cov = scipy.interpolate.interp1d(r_1d, norm_cov_1d, kind='quadratic', axis=1, 
                                         bounds_error=False, fill_value=0)(r)
        
        return self.params[-1][0] * cov
  
        
    
class MKern(object):
    ''' extension of kernel for regression in multiple baselines range'''
    
    def __init__(self, n_bins, kern_class, variance=1, lengthscale=1, alpha=0, name='mkern'):
        self.n_bins = n_bins
        self.kern_class = kern_class
        kern_class.__init__(self, 1, variance=variance, lengthscale=lengthscale, name=name)
        self.alpha = GPy.core.parameterization.Param('alpha', alpha)
        self.alpha.set_prior(UniformPrior(-2, 2))
        self.link_parameters(self.alpha)
        self.kerns = [self.kern_class(1) for i in range(self.n_bins)]
        self.alpha = alpha

    def parameters_changed(self):
        for i in range(self.n_bins):
            self.kerns[i].variance = self.variance[0]
            self.kerns[i].lengthscale = np.clip(self.lengthscale[0] * (1 + self.alpha * (i + 1)), 1e-8, 1e8)
        
    def K(self, X, X2=None):
        return np.array([k.K(X, X2) for k in self.kerns])
           

class MRBF(MKern, GPy.kern.RBF):
    
    def __init__(self, n_bins, variance=1, lengthscale=1, alpha=0, name='mrbf'):
        MKern.__init__(self, n_bins, GPy.kern.RBF, variance=variance, lengthscale=lengthscale, 
                       alpha=alpha, name=name)


class MMat32(MKern, GPy.kern.Matern32):
    
    def __init__(self, n_bins, variance=1, lengthscale=1, alpha=0, name='mmat32'):
        MKern.__init__(self, n_bins, GPy.kern.Matern32, variance=variance, lengthscale=lengthscale, 
                       alpha=alpha, name=name)


class MMat52(MKern, GPy.kern.Matern52):
    
    def __init__(self, n_bins, variance=1, lengthscale=1, alpha=0, name='mmat52'):
        MKern.__init__(self, n_bins, GPy.kern.Matern52, variance=variance, lengthscale=lengthscale, 
                       alpha=alpha, name=name)

class MExponential(MKern, GPy.kern.Exponential):
    
    def __init__(self, n_bins, variance=1, lengthscale=1, alpha=0, name='mexp'):
        MKern.__init__(self, n_bins, GPy.kern.Exponential, variance=variance, lengthscale=lengthscale, 
                       alpha=alpha, name=name)


class MWhiteHeteroscedastic(GPy.kern.Kern):
    
    def __init__(self, var_noise, name='noise'):
        GPy.kern.Kern.__init__(self, 1, 0, name)
        self.var_noise = var_noise
        self.alpha = GPy.core.parameterization.Param('alpha', 1)
        self.alpha.constrain_fixed()
        self.link_parameters(self.alpha)

    def K(self, X, X2=None):
        return [self.alpha[0] * np.diag(v) for v in self.var_noise]
        

class GPRegressor:
    ''' Simple GPR. See e.g. http://www.gaussianprocess.org/gpml/chapters/RW2.pdf'''

    def __init__(self, X, Y, K):
        self.X = X
        self.K = K
        self.Y = Y
        self.fit()
        
    def fit(self):
        self.L_ = GPy.util.linalg.jitchol(self.K, maxtries=100)
        self.alpha_, _ = GPy.util.linalg.dpotrs(self.L_, self.Y, lower=1)

    def predict(self, K_star):
        y_mean = K_star.dot(self.alpha_)
        v, _ = GPy.util.linalg.dpotrs(self.L_, K_star.T, lower=1)
        y_cov = K_star - K_star.dot(v)
        return y_mean, y_cov
    
    def log_marginal_likelihood(self):
        return - 0.5 * (self.Y.size *  np.log(2 * np.pi) + 2 * self.Y.shape[1] * np.sum(np.log(np.diag(self.L_))) + np.sum(self.alpha_ * self.Y))


class MultiGPRegressor(GPy.core.model.Model):
    ''' Extension of GPRegressor to support multi-baselines '''
    
    def __init__(self, X, Ys, kern, name='mgp'):
        super(MultiGPRegressor, self).__init__(name=name)
        self.kern = kern
        self.X = X
        self.Ys = Ys
        self.gp_regressors = None
        self.link_parameters(self.kern)

    def fit(self):
        Ks = self.kern.K(self.X)
        if Ks.ndim == 2 and self.Ys.ndim == 2:
            self.gp_regressors = [GPRegressor(self.X, self.Ys, Ks)]
        else:
            self.gp_regressors = [GPRegressor(self.X, Y, K) for K, Y in zip(Ks, self.Ys)]
    
    def predict(self, kern=None):
        assert self.gp_regressors is not None
        if kern is None:
            kern = self.kern
        Ks = kern.K(self.X)
        if Ks.ndim == 2:
            Ks = np.repeat(Ks[None], len(self.Ys), axis=0)
        return [gp_regressor.predict(K) for K, gp_regressor in zip(Ks, self.gp_regressors)]
    
    def log_marginal_likelihood(self):
        assert self.gp_regressors is not None
        return np.sum([gp_regressor.log_marginal_likelihood() for gp_regressor in self.gp_regressors])


class UniformPrior(object):

    domain = GPy.priors._REAL

    def __init__(self, l, u):
        self.lower = l
        self.upper = u

    def __str__(self):
        return "[{:.2g}, {:.2g}]".format(self.lower, self.upper)

    def lnpdf(self, x):
        region = (x >= self.lower) * (x <= self.upper)
        return np.log(region * np.e)

    def lnpdf_grad(self, x):
        return np.zeros(x.shape)

    def rvs(self, n):
        return np.random.uniform(self.lower, self.upper, size=n)

class UniformPriorPos(object):

    domain = GPy.priors._POSITIVE

    def __init__(self, l, u):
        self.lower = l
        self.upper = u

    def __str__(self):
        return "[{:.2g}, {:.2g}]".format(self.lower, self.upper)

    def lnpdf(self, x):
        region = (x >= self.lower) * (x <= self.upper)
        return np.log(region * np.e)

    def lnpdf_grad(self, x):
        return np.zeros(x.shape)

    def rvs(self, n):
        return np.random.uniform(self.lower, self.upper, size=n)


class PsStacker(object):

    def __init__(self, ps_gen, kbins):
        self.all_ps = []
        self.all_ps2d = []
        self.all_var = []
        self.ps_gen = ps_gen
        self.kbins = kbins

    def add(self, cube):
        self.all_ps.append(ps_gen.get_ps3d(self.kbins, cube))
        self.all_ps2d.append(ps_gen.get_ps2d(cube))
        self.all_var.append(ps_gen.get_variance(cube))

    def get_ps2d(self):
        return CylindricalPowerSpectraMC(self.all_ps2d)

    def get_variance(self):
        return VarianceMC(self.all_var)

    def get_ps3d(self):
        return SphericalPowerSpectraMC(self.all_ps)


class DataMangler(object):
    
    def __init__(self, i_cube, uv_bins, norm_factor=1):
        self.i_cube = i_cube
        self.X = (i_cube.freqs * 1e-6)[:, None]
        self.norm_factor = norm_factor
        self.uv_bins = uv_bins
        self.c2f = lambda c: np.concatenate([c.real, c.imag], axis=1)
        self.f2c = lambda f: f[:, :f.shape[1] // 2] + 1j * f[:, f.shape[1] // 2:]
        
    def split(self, i_cube):
        idxs = [(i_cube.ru >= umin) & (i_cube.ru <= umax) for umin, umax in self.uv_bins]
        Ys = [i_cube.data[:, idx] for idx in idxs]

        return [self.c2f(Y * self.norm_factor) for Y in Ys]
    
    def variance_split(self, v_cube, axis=1):
        return [Y.var(axis=axis) for Y in self.split(v_cube)]
    
    def unsplit(self, Ys):
        cube = self.i_cube.copy()
        idxs = [(cube.ru >= umin) & (cube.ru <= umax) for umin, umax in self.uv_bins]
        for Y, idx in zip(Ys, idxs):
            cube.data[:, idx] = self.f2c(Y)
        return 1 / self.norm_factor * cube

    def gen_cube(self, Ys_and_covYs):
        cube = self.i_cube.copy()
        idxs = [(cube.ru >= umin) & (cube.ru < umax) for umin, umax in self.uv_bins]
        for (Y, covY), idx in zip(Ys_and_covYs, idxs):
            cube.data[:, idx] = self.f2c(Y) + get_samples(self.X, idx.sum(), covY)
        return 1 / self.norm_factor * cube


def get_kern_part(kern, name):
    if kern.name == name:
        return kern

    kern_list = []
    for k in kern.parts:
        if fnmatch.fnmatch(k.name, name):
            kern_list.append(k)
    if len(kern_list) == 0:
        return None
    elif len(kern_list) == 1:
        return kern_list[0]
    return GPy.kern.Add(kern_list)

    
def run_mcmc(gp, nsteps, nwalkers, lower_bound, upper_bound, verbose=False, save_file=None, continue_previous=False):
    def lnprob(p):
        gp.kern.optimizer_array = p
        if not np.isfinite(gp.kern.log_prior()):
            return - np.inf
        gp.fit()
        log_marginal_likelihood = gp.log_marginal_likelihood()
        if verbose:
            print(gp.kern.param_array, log_marginal_likelihood, gp.kern.log_prior())
        return log_marginal_likelihood + gp.kern.log_prior()

    ndim = len(gp.kern.optimizer_array)
    
    pos = np.random.uniform(low=np.array(lower_bound)[:, None], 
                            high=np.array(upper_bound)[:, None], size=(ndim, nwalkers)).T

    if save_file is not None:
        backend = emcee.backends.HDFBackend(save_file)
        if not continue_previous:
            backend.reset(nwalkers, ndim)
        sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, backend=backend)
    else:
        sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob)

    try:
        pr = psutil.progress_report(nsteps)
        for i, result in enumerate(sampler.sample(pos, iterations=nsteps)):
            pr(i)
            if i % 20 == 0:
                print('Last 20:')
                print('Median:', ', '.join([f'{k:.3f}' for k in np.median(sampler.chain[:, -20:], axis=(0, 1))]))
                print('Mean:', ', '.join([f'{k:.3f}' for k in np.mean(sampler.chain[:, -20:], axis=(0, 1))]))
                print('Min:', ', '.join([f'{k:.3f}' for k in np.min(sampler.chain[:, -20:], axis=(0, 1))]))
                print('Max:', ', '.join([f'{k:.3f}' for k in np.max(sampler.chain[:, -20:], axis=(0, 1))]))
                print('Rms:', ', '.join([f'{k:.3f}' for k in np.std(sampler.chain[:, -20:], axis=(0, 1))]))
                print(f'Likelihood: {sampler.lnprobability[:, -20:].mean():.2f} +-{sampler.lnprobability[:, -20:].std():-2f}')
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        
    return sampler

def load_mcmc(save_file):
    return emcee.backends.HDFBackend(save_file)


def get_mc_samples(sampler, nburn=50, clip_nsigma=5):
    nsteps, nwalkers, nparams = sampler.get_chain().shape
    samples = sampler.get_chain(discard=nburn).reshape((-1, nparams))

    samples_outliers = np.zeros_like(samples)
    for i in range(samples.shape[1]):
        m = np.median(samples[:, i])
        s = psutil.robust_std(samples[:, i])
        samples_outliers[abs(samples[:, i] - m) > clip_nsigma * s, i] = 1

    return samples[samples_outliers.sum(axis=1) == 0]


def plot_samples(sampler):
    nsteps, nwalkers, nparams = sampler.get_chain().shape

    ncols = 4
    nrows = int(np.ceil(nparams / ncols))

    fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=(12, 1 + 2.2 * nrows), sharex=True)

    auto_cors = sampler.get_autocorr_time(tol=0)
    chain = sampler.get_chain()

    for j, ax in zip(range(nparams), axs.flatten()):
        ax.plot(chain[:, :, j], c='tab:orange', alpha=0.6)
        ax.axvline(auto_cors[j], c=psutil.black, ls=':')
        ax.axvline(5 * auto_cors[j], c=psutil.black, ls='--')
        if (np.median(chain[:, :, j]) < 1) and np.all(chain[:, :, j].flatten() > 1e-8):
            ax.set_yscale('log')

    fig.tight_layout(pad=0.15)
    
    return fig


def plot_samples_likelihood(sampler, p_true=None, n_burn=0):
    nsteps, nwalkers, nparams = sampler.get_chain().shape

    ncols = 4
    nrows = int(np.ceil(nparams / ncols))

    fig, axs = plt.subplots(ncols=ncols, nrows=nrows, figsize=(12, 1 + 2.5 * nrows), sharey=True)

    y = - sampler.get_log_prob(discard=n_burn).flatten()
    chain = sampler.get_chain(discard=n_burn)
    i = np.repeat(np.arange(chain.shape[0])[:, None], nwalkers, axis=1).flatten()

    for j, ax in zip(range(nparams), axs.flatten()):
        x = chain[:, :, j].flatten()
        ax.scatter((x), astats.sigma_clip(y), marker='+', c=i, cmap='viridis')
        ax.set_yscale('log')
        if p_true is not None:
            ax.axvline(p_true[j], c='tab:orange', ls='--')
    fig.tight_layout(pad=0.15)
    
    return fig


def plot_corner(sampler, n_burn):
    samples_filter = get_mc_samples(sampler, n_burn)

    return corner.corner(samples_filter, plot_datapoints=False, smooth=0.8, quantiles=(0.16, 0.84))


def get_ps_stack(gp, sampler, data_mangler, ps_stacker, n_burn, n_pick=100, kern_name='eor', 
                 subtract_from=None, verbose=False):
    samples = get_mc_samples(sampler, nburn=n_burn, clip_nsigma=5)
    pick = np.random.randint(0, samples.shape[0], n_pick)
    pr = psutil.progress_report(len(pick))
    for j, i in enumerate(pick):
        pr(j)
        m_oa = samples[i].copy()
        gp.kern.optimizer_array = m_oa
        gp.fit()
        if verbose:
            print(m_oa)
        c_rec = data_mangler.gen_cube(gp.predict(get_kern_part(gp.kern, kern_name)))
        if subtract_from is not None:
            c_rec = subtract_from - c_rec
        ps_stacker.add(c_rec)
        
    return ps_stacker


class SphericalPowerSpectraMC(pspec.SphericalPowerSpectra):

    def __init__(self, ps3d_all):
        self.all_ps = ps3d_all
        m = np.median([ps.data for ps in self.all_ps], axis=0)
        std = psutil.robust_std([ps.data for ps in self.all_ps], axis=0)
        pspec.SphericalPowerSpectra.__init__(self, m, std, self.all_ps[0].k_bins, self.all_ps[0].k_mean, 
                                             n_eff=self.all_ps[0].n_eff, k_std=self.all_ps[0].k_std)
        self.q16 = np.quantile(np.array([ps.data for ps in self.all_ps]), .16, axis=0)
        self.q84 = np.quantile(np.array([ps.data for ps in self.all_ps]), .84, axis=0)
        self.q2_5 = np.quantile(np.array([ps.data for ps in self.all_ps]), .025, axis=0)
        self.q97_5 = np.quantile(np.array([ps.data for ps in self.all_ps]), .975, axis=0)

    def plot(self, ax=None, show68=True, show95=True, marker='+', mkelvin=True, kelvin_square=True,
             title=None, kerr_as_kbins=False, **kargs):
        if ax is None:
            fig, ax = plt.subplots()

        d, e, temp_unit = self.temp_conversion(self.data, self.err, mkelvin=mkelvin, kelvin_square=kelvin_square)
        
        if show68:
            q16, _, _ = self.temp_conversion(self.q16, self.err, mkelvin=mkelvin, kelvin_square=kelvin_square)
            q84, _, _ = self.temp_conversion(self.q84, self.err, mkelvin=mkelvin, kelvin_square=kelvin_square)
            ax.fill_between(self.k_mean, q16, q84, alpha=kargs.get('alpha', 0.5), color=kargs.get('c', None))
        if show95:
            q2_5, _, _ = self.temp_conversion(self.q2_5, self.err, mkelvin=mkelvin, kelvin_square=kelvin_square)
            q97_5, _, _ = self.temp_conversion(self.q97_5, self.err, mkelvin=mkelvin, kelvin_square=kelvin_square)
            ax.fill_between(self.k_mean, q2_5, q97_5, alpha=0.5 * kargs.get('alpha', 0.5), color=kargs.get('c', None))

        ax.plot(self.k_mean, d, marker=marker, **kargs)

        ax.set_yscale('log', **pspec.nonpos_arg)
        ax.set_xscale('log')

        ax.set_ylabel(r'$\Delta%s (k)\,[\mathrm{%s}]$' % ('^2' * kelvin_square, temp_unit))
        ax.set_xlabel(r'$k\,[\mathrm{h\,cMpc^{-1}}]$')

        ax.set_xlim(self.k_bins.min(), self.k_bins.max())

        if title is not None:
            ax.set_title(title)

            
class CylindricalPowerSpectraMC(pspec.CylindricalPowerSpectra):

    def __init__(self, all_ps2d):
        self.all_ps2d = all_ps2d
        ps0 = self.all_ps2d[0]
        m = np.median([ps.data for ps in self.all_ps2d], axis=0)
        std = psutil.robust_std([ps.data for ps in self.all_ps2d], axis=0)
        
        pspec.CylindricalPowerSpectra.__init__(self, m, std, ps0.delay, ps0.el, ps0.k_per, ps0.k_par, 
                                               n_eff=ps0.n_eff, ps2d_w=ps0.w)
        
        self.q16 = np.quantile(np.array([ps.data for ps in self.all_ps2d]), .16, axis=0)
        self.q84 = np.quantile(np.array([ps.data for ps in self.all_ps2d]), .84, axis=0)
        self.q2_5 = np.quantile(np.array([ps.data for ps in self.all_ps2d]), .025, axis=0)
        self.q97_5 = np.quantile(np.array([ps.data for ps in self.all_ps2d]), .975, axis=0)

    def plot_kpar(self, ax=None, show68=True, show95=True, delay=False, weighted=True, **kargs):
        if ax is None:
            fig, ax = plt.subplots()

        if weighted and isinstance(self.w, np.ndarray):
            y, q16, q84, q2_5, q97_5 = psutil.nanaverage(np.array([self.data, self.q16, self.q84, 
                                                                   self.q2_5, self.q97_5]), 
                                                         self.w[None], axis=2)
        else:
            y, q16, q84, q2_5, q97_5 = np.nanmean([self.data, self.q16, self.q84, self.q2_5, self.q97_5], 
                                                  axis=2)

        if delay:
            x = self.delay
        else:
            x = self.k_par

        if show68:
            ax.fill_between(x, q16, q84, alpha=kargs.get('alpha', 0.5), color=kargs.get('c', None))
        if show95:
            ax.fill_between(x, q2_5, q97_5, alpha=0.5 * kargs.get('alpha', 0.25), color=kargs.get('c', None))

        ax.plot(x, y, **kargs)

        ax.set_yscale('log', **pspec.nonpos_arg)

        if delay:
            ax.set_xlabel('Delay (us)')
        else:
            ax.set_xlabel(r'$k_{\parallel}\,[\mathrm{h\,cMpc^{-1}}]$')

        ax.set_ylabel(r'$P(k_{\parallel})\,[\mathrm{K^2\,h^{-3}\,cMpc^3}]$')

    def plot_kper(self, ax=None, show68=True, show95=True, normalize=False, weighted=True, **kargs):
        if ax is None:
            fig, ax = plt.subplots()

        if weighted and isinstance(self.w, np.ndarray):
            y, q16, q84, q2_5, q97_5 = psutil.nanaverage(np.array([self.data, self.q16, self.q84, 
                                                                   self.q2_5, self.q97_5]), 
                                                         self.w[None], axis=1)
        else:
            y, q16, q84, q2_5, q97_5 = np.nanmean([self.data, self.q16, self.q84, self.q2_5, self.q97_5], 
                                                  axis=1)
        if normalize:
            n = self.k_per ** 2 / (2 * np.pi)
            y, q16, q84, q2_5, q97_5 = [n * k for k in (y, q16, q84, q2_5, q97_5)]

        x = self.k_per

        if show68:
            ax.fill_between(x, q16, q84, alpha=kargs.get('alpha', 0.5), color=kargs.get('c', None))
        if show95:
            ax.fill_between(x, q2_5, q97_5, alpha=0.5 * kargs.get('alpha', 0.25), color=kargs.get('c', None))

        ax.plot(x, y, **kargs)

        ax.set_yscale('log', **pspec.nonpos_arg)

        ax.set_xlabel(r'$k_{\bot}\,[\mathrm{h\,cMpc^{-1}}]$')

        if normalize:
            ax.set_ylabel(r'$\Delta^2 (k_{\bot})\,[\mathrm{K^2}]$')
        else:
            ax.set_ylabel(r'$P(k_{\bot})\,[\mathrm{K^2\,h^{-3}\,cMpc^3}]$')


class VarianceMC(pspec.Variance):

    def __init__(self, all_var):
        v0 = all_var[0]
        self.all_var = all_var
        m = np.median([ps.data for ps in self.all_var], axis=0)
        std = psutil.robust_std([ps.data for ps in self.all_var], axis=0)
          
        pspec.Variance.__init__(self, m, std, v0.freqs, var_w=v0.w)

        self.q16 = np.quantile(np.array([ps.data for ps in self.all_var]), .16, axis=0)
        self.q84 = np.quantile(np.array([ps.data for ps in self.all_var]), .84, axis=0)
        self.q2_5 = np.quantile(np.array([ps.data for ps in self.all_var]), .025, axis=0)
        self.q97_5 = np.quantile(np.array([ps.data for ps in self.all_var]), .975, axis=0)

    def plot(self, ax=None, show68=True, show95=True, mkelvin=True, title=None, **kargs):
        if ax is None:
            fig, ax = plt.subplots()

        a = 1
        if mkelvin:
            a = 1e6
            
        d, q2_5, q16, q84, q97_5 = a * np.array([self.data, self.q2_5, self.q16, self.q84, self.q97_5])
        f = self.freqs * 1e-6

        if show68:
            ax.fill_between(f, q16, q84, alpha=kargs.get('alpha', 0.5), color=kargs.get('c', None))
        if show95:
            ax.fill_between(f, q2_5, q97_5, alpha=0.5 * kargs.get('alpha', 0.25), color=kargs.get('c', None))

        ax.plot(f, d, **kargs)
        
        ax.set_yscale('log', **pspec.nonpos_arg)
        ax.set_xlabel(r"$\mathrm{Frequency\,[MHz]}$")

        if mkelvin:
            ax.set_ylabel(r"$\mathrm{Variance\,[mK^2]}$")
        else:
            ax.set_ylabel(r"$\mathrm{Variance\,[K^2]}$")

        if title is not None:
            ax.set_title(title)


def plot_ps_results(ps_stacker, v_cube, e_cube=None, ev_cube=None, extras=()):
    kbins = ps_stacker.kbins
    ps_gen = ps_stacker.ps_gen
    if ev_cube is None and e_cube is not None:
        ev_cube = 1e-10 * e_cube
        
    colors = ['tab:green', 'tab:orange', 'tab:magenta']

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(ncols=2, nrows=2, figsize=(10, 8))
    ps_gen.get_ps2d(v_cube).plot_kpar(ax=ax3, label='noise', c='tab:blue')
    ps_stacker.get_ps2d().plot_kpar(ax=ax3, label='recovered', c=psutil.black, alpha=0.4)
    if e_cube is not None:
        (ps_gen.get_ps2d(e_cube) - ps_gen.get_ps2d(ev_cube)).plot_kpar(ax=ax3, label='21', 
                                                                       c='tab:red', ls='--', lw=2)
        
    for extra, c in zip(extras, colors):
        ps_gen.get_ps2d(extra[0]).plot_kpar(ax=ax3, label=extra[1], c=c)

    ps_gen.get_ps2d(v_cube).plot_kper(ax=ax4, label='noise', c='tab:blue')
    ps_stacker.get_ps2d().plot_kper(ax=ax4, label='recovered', c=psutil.black, alpha=0.4)
    if e_cube is not None:
        (ps_gen.get_ps2d(e_cube) - ps_gen.get_ps2d(ev_cube)).plot_kper(ax=ax4, label='21', 
                                                                       c='tab:red', ls='--', lw=2)
    for extra, c in zip(extras, colors):
        ps_gen.get_ps2d(extra[0]).plot_kper(ax=ax4, label=extra[1], c=c)

    if e_cube is not None:
        (ps_gen.get_variance(e_cube) - ps_gen.get_variance(ev_cube)).plot(ax=ax1, label='21',  
                                                                          c='tab:red', ls='--', lw=2)
    ps_stacker.get_variance().plot(ax=ax1, label='recovered', c=psutil.black, alpha=0.4)
    ps_gen.get_variance(v_cube).plot(ax=ax1, label='noise')

    for extra, c in zip(extras, colors):
        ps_gen.get_variance(extra[0]).plot(ax=ax1, label=extra[1], c=c)

    if e_cube is not None:
        ps_gen.get_ps3d_with_noise(kbins, e_cube, ev_cube).plot(ax=ax2, label='21', c='tab:red', 
                                                                lw=2, ls='--', marker='', nsigma=0)
    ps_gen.get_ps3d(kbins, v_cube).plot(ax=ax2, label='noise', c='tab:blue')
    ps_stacker.get_ps3d().plot(ax=ax2, label='recovered', c=psutil.black, alpha=0.4)
    
    for extra, c in zip(extras, colors):
        ps_gen.get_ps3d(kbins, extra[0]).plot(ax=ax2, label=extra[1], c=c)

    lgd = fig.legend(*ax1.get_legend_handles_labels(),
                      bbox_to_anchor=(0.5, 1.04), loc="upper center", ncol=3)
    fig.tight_layout()


class Exponent(paramz.transformations.Transformation):
    domain = paramz.transformations._POSITIVE

    def f(self, x):
        return 10 ** x

    def finv(self, x):
        return np.log10(x)

    def initialize(self, f):
        if np.any(f < 0.):
            logger.info("Warning: changing parameters to satisfy constraints")
        return np.abs(f)

    def __str__(self):
        return 'exp'



class MLGPRConfig(object):

    def __init__(self, kern, params_init_lower, params_init_upper, uv_bins, n_walkers, n_samples):
        self.kern = kern
        self.lower = params_init_lower
        self.upper = params_init_upper
        self.uv_bins = uv_bins
        self.n_walkers = n_walkers
        self.n_samples = n_samples

    def load_from_script(self, filename):
        loader = importlib.machinery.SourceFileLoader("config_script", filename)
        config_script = loader.load_module("config_script")

        return MLGPRConfig(config_script.kern, config_script.lower, config_script.upper, 
                           config_script.uv_bins, config_script.norm_factor, config_script.n_walkers
                           config_script.n_samples)


class MLGPRFit(object):

    def __init__(self, i_cube, noise_cube, ml_gpr_config, name):
        self.i_cube = i_cube
        self.noise_cube = noise_cube
        self.config = ml_gpr_config
        self.name = name

    def run(self):
        norm_factor = np.sqrt(1 / self.i_cube.data.real.var())
        data_mangler = DataMangler(self.i_cube, self.config.uv_bins, self.config.norm_factor)
        gp = MultiGPRegressor(data_mangler.X, data_mangler.split(self.i_cube), self.config.kern)
        sampler = run_mcmc(gp, self.config.n_samples, self.config.n_walkers, self.config.lower, 
                           self.config.upper, False, save_file=name)


class MLGPRResult(object):

    def __init__(self, i_cube, noise_cube, ml_gpr_config, sampler):
        self.i_cube = i_cube
        self.noise_cube = noise_cube
        self.config = ml_gpr_config
        self.sampler = sampler

    def get_ps_stack(self, kbins, kern_name, n_burn=None):
        norm_factor = np.sqrt(1 / self.i_cube.data.real.var())
        data_mangler = DataMangler(self.i_cube, self.config.uv_bins, self.config.norm_factor)
        gp = MultiGPRegressor(data_mangler.X, data_mangler.split(self.i_cube), self.config.kern)
        return get_ps_stack(gp, self.sampler, data_mangler, PsStacker(ps_gen, kbins), n_burn, kern_name=kern_name)

    def save(self, name):
        # Save config script
        # Save sampler 
        # Save i_cube, noise_cube
        pass

    def load(self, name)




obs_id = 'L246309_nouter_flagged'
# obs_id = 'C_all_nouter_014'

data_path = f'/net/node100/data/users/lofareor/mertens/ncp_np5_red3/np4_v02_dd_1c_flag/vis_cubes_u50-250_fov4/{obs_id}/'
conf_path = '/home/users/mertens/projects/NCP/nights_np5_red3//config/'

i_cube = datacube.CartDataCube.load(data_path + f'{obs_id}_Ibt_fov4_u50-250.h5')
v_cube = datacube.CartDataCube.load(data_path + f'{obs_id}_Vbt_fov4_u50-250.h5')

noise_cube_dt = datacube.CartDataCube.load(data_path + f'{obs_id}_dt_Vbt_fov4_u50-250.h5')
# noise_cube = noise_cube_dt

w = i_cube.weights.copy()
w.scale_with_noise_cube(i_cube.make_diff_cube(), 3)
noise_cube = w.simulate_noise(2500, i_cube.meta.total_time)

flagger_runner = flagger.FlaggerRunner.load(conf_path + 'flagger_extened_ateam.parset')
i_cube, v_cube = flagger_runner.run(i_cube, v_cube)
noise_cube = flagger_runner.flag.apply(noise_cube)
flagger_runner.plot()

ps_gen = ps_build.get(i_cube, fmhz_range=[122, 134], du=8, umax=250, umin=50, rmean_freqs=True, ps2d_pos_only=True)
kbins = np.logspace(np.log10(ps_gen.kmin), np.log10(1), 9)

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 4))
ps_gen.get_ps2d(i_cube).plot_kpar(ax=ax1, label='I')
ps_gen.get_ps2d(noise_cube).plot_kpar(ax=ax1, label='noise')
ps_gen.get_ps2d(noise_cube_dt).plot_kpar(ax=ax1, label='noise dt')

ps_gen.get_ps3d(kbins, i_cube).plot(ax=ax2, label='I')
ps_gen.get_ps3d(kbins, noise_cube).plot(ax=ax2, label='noise')
ps_gen.get_ps3d(kbins, noise_cube_dt).plot(ax=ax2, label='noise dt')
ax1.legend()
ax2.legend()
fig.tight_layout()


norm_factor = 1e2
uv_bins = psutil.pairwise(np.arange(50, 275, 15))

k_fg = MRBF(len(uv_bins), name='fg1') 
k_fg += MMat32(len(uv_bins), name='fg2')
k_fg += MMat32(len(uv_bins), name='fg3')

k_eor = VAEKern(decoder, 2, i_cube.freqs, uv_bins, name='eor1')

k_noise = MWhiteHeteroscedastic(data_mangler.variance_split(noise_cube), name='noise')

k = k_fg + k_eor + k_noise

k.fg1.variance.unconstrain()
k.fg1.variance.set_prior(UniformPrior(1e0, 1e3))
k.fg1.lengthscale.unconstrain()
k.fg1.lengthscale.set_prior(UniformPrior(1.5, 60))
k.fg1.alpha.constrain_fixed()

k.fg2.variance.unconstrain()
k.fg2.variance.set_prior(UniformPrior(1e-3, 100))
k.fg3.variance.unconstrain()
k.fg3.variance.set_prior(UniformPrior(1e-3, 100))

k.eor1.x1.set_prior(GPy.core.parameterization.priors.Gaussian(0, 1))
k.eor1.x2.set_prior(GPy.core.parameterization.priors.Gaussian(0, 1))
k.eor1.variance.unconstrain()
k.eor1.variance.constrain(Exponent())
k.eor1.variance.set_prior(UniformPriorPos(-20, 20))

k.noise.alpha.unconstrain()
k.noise.alpha.set_prior(UniformPrior(0.9, 1.6))

k

tr = lambda x: np.log(np.expm1(x))
in_tr = lambda x: np.log1p(np.exp(x))

upper = [1.3 * norm_factor ** 2 * i_cube.data.real.var(), tr(20), 
         20, tr(8), 0.1, 
         20, tr(3), 0.1, 
         3, 3, 2, 
         1.4]

lower = [1 * norm_factor ** 2 * i_cube.data.real.var(), tr(10),
         0.1, tr(2), -0.1,
         0.1, tr(1), -0.1, 
         -3, -3, -2,
         1]


data_mangler = DataMangler(i_cube, uv_bins, norm_factor)
gp = MultiGPRegressor(data_mangler.X, data_mangler.split(i_cube), k)
sampler = run_mcmc(gp, 600, 50, lower, upper, False, 
                   save_file=f'mcmc_ncp_{obs_id}_red3_8.h5')
# sampler = load_mcmc(f'mcmc_ncp_{obs_id}_red3_6.h5')



Configuration: k, uv_bins, upper lower

Configuration:

kern.uv_bins_du = 15

[kern.fg]
int.type = MRBF
int.variance.prior = 'Uniform(1, 1e3)'
int.variance.mc_bounds = [0.5, 1.2]
int.lengthscale.prior = 'Uniform(1, 1e3)'
int.lengthscale.mc_bounds = [2, 60]
int.alpha.prior = 'Fixed(0)'


[kern.eor]
vae.type = VAEKern
vae.decoder_filename = 'some_file'
vae.latent_dim = 2


[kern.noise]
alpha.mc_bounds = [0.9, 1.6]

[mcmc]
n_steps = 600
n_walkers = 50


ps_eor = get_ps_stack(gp, sampler, data_mangler, PsStacker(ps_gen, kbins), 300, kern_name='eor*')
