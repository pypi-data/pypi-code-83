import numpy as np
from tqdm import tqdm
import scipy.integrate as integrate

from .core import crank_nicolson


def logistic_damping(I_linspace, I0, damping_point, lenght):
    """Performs a logistic damping on the given point
    of a particle distribution.
    
    Parameters
    ----------
    I_linspace : numpy 1D array
        Coordinates on which you want to work
    I0 : numpy 1D array
        Distribution on which you perform the damping
    damping_point : float
        Corresponding point on which you perform the damping
    lenght : float
        Lenght of the damping (damping point is in the middle)
    
    Returns
    -------
    numpy 1D array
        New damped distribution
    """
    I1 = I0 * (1 - 1 / (1 + 1/np.exp((I_linspace - damping_point)/lenght)))
    return I1


class cn_polynomial(object):
    def __init__(self, I_max, c, exponent, I0, dt, normalize=True, I_min=0.0, I_star=1.0):
        self.I_max = I_max
        self.I_min = I_min
        self.c = c
        self.exponent = exponent
        self.I0 = I0
        
        self.dt = dt
        self.samples = len(I0)

        self.I = np.linspace(I_min, I_max, self.samples)
        self.I_star = I_star
        self.dI = np.absolute(self.I[1] - self.I[0])
        self.half_dI = self.dI * 0.5

        self.locked_left = False
        self.locked_right = False

        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, I_star)) if \
                (i - self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        # For Reference:
        self.diffusion = self.poly_D(self.I, I_star)

        # Normalize?
        if normalize:
            self.I0 /= integrate.trapz(self.I0, x=self.I)

        self.engine = crank_nicolson(
            self.samples, I_min, I_max, self.dt, self.I0.copy(), A, B, C, D)

    def poly_D(self, I, I_star=1.0):
        return self.c * np.power(I / I_star, self.exponent)

    def set_source(self, source):
        """Apply a source vector to the simulation, this will overwrite all non zero values over the simulation distribution at each iteration.
        
        Parameters
        ----------
        source : ndarray
            source to apply
        """
        self.engine.set_source(source)

    def remove_source(self):
        """Remove the source vector to the simulation.
        """
        self.engine.remove_source()

    def lock_left(self):
        """Lock the left boundary to the non-zero value it has right now.
        """
        self.engine.set_lock_left()
        self.locked_left = True

    def lock_right(self):
        """Lock the right boundary to the non-zero value it has right now.
        """
        self.engine.set_lock_right()
        self.locked_right = True

    def unlock_left(self):
        """Unlock the left boundary and set it to zero.
        """
        self.engine.unlock_left()
        self.locked_left = False

    def unlock_right(self):
        """Unlock the right boundary and set it to zero.
        """
        self.engine.unlock_right()
        self.locked_right = False

    def extend(self, I_max):
        """Extends the size of the simulation and moves forward the absorbing
        barrier.
        
        Parameters
        ----------
        I_max : float
            new position for absorbing barrier
        """
        assert self.I_max < I_max
        extension = np.arange(self.I_max, I_max, self.dI)[1:]
        extension = np.append(extension, extension[-1] + self.dI)

        self.I = np.append(self.I, extension)
        self.I_max = self.I[-1]

        increasing = len(self.I) - self.samples
        self.samples = len(self.I)

        self.I0 = np.append(self.I0, np.zeros(increasing))
        data = np.append(np.array(self.engine.x), np.zeros(increasing))
        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, self.I_star)) if (i -
                                                       self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, self.I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        N = self.engine.executed_iterations
        self.engine = crank_nicolson(
            self.samples, self.I_min, self.I[-1], self.dt, data, A, B, C, D)
        if self.locked_left:
            self.engine.set_lock_left()
        if self.locked_right:
            self.engine.set_lock_right()

        self.engine.set_executed_iterations(N)

        self.diffusion = self.poly_D(self.I, self.I_star)

    def cut(self, damping_point, length, I_max=-1.0):
        """Executes a damping of the distribution and, if required, reduces
        the size of the simulation.
        
        Parameters
        ----------
        damping_point : float
            point of damping
        length : float
            lenght of the damping
        I_max : float, optional
            new position for the absorbing barrier, by default -1.0
        """
        assert self.I_max > I_max
        assert self.I_max > damping_point

        # Logistic damping at given point
        new_data = logistic_damping(
            self.I, self.engine.x, damping_point, length)

        # Are we moving the collimator?
        if I_max != -1.0:
            assert damping_point <= I_max
            new_I = np.arange(self.I_min, I_max, self.dI)
            new_I = np.append(new_I, new_I[-1] + self.dI)

            self.I = new_I
            self.I_max = self.I[-1]

            self.I0 = self.I0[:len(self.I)]
            self.samples = len(self.I)
            new_data = new_data[:len(self.I)]

        # Let's make everything again
        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, self.I_star)) if (i -
                                                       self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, self.I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        N = self.engine.executed_iterations
        self.engine = crank_nicolson(
            self.samples, self.I[0], self.I[-1], self.dt, new_data, A, B, C, D)
        if self.locked_left:
            self.engine.set_lock_left()
        if self.locked_right:
            self.engine.set_lock_right()

        self.engine.set_executed_iterations(N)

        self.diffusion = self.poly_D(self.I, self.I_star)

    def change_dt(self, new_dt):
        """Change the dt of the integrator.
        
        Parameters
        ----------
        new_dt : float
            New value for dt
        """
        data = np.array(self.engine.x)
        self.dt = new_dt

        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, self.I_star)) if (i -
                                                       self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, self.I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        N = self.engine.executed_iterations
        self.engine = crank_nicolson(
            self.samples, self.I[0], self.I[-1], self.dt, data, A, B, C, D)
        if self.locked_left:
            self.engine.set_lock_left()
        if self.locked_right:
            self.engine.set_lock_right()

        self.engine.set_executed_iterations(N)

    def iterate(self, n_iterations):
        """Iterates the simulation.
        
        Parameters
        ----------
        n_iterations : int
            number of iterations to perform
        """
        self.engine.iterate(n_iterations)

    def reset(self):
        """Resets the simulation to the starting condition.
        """
        self.engine.reset()

    def get_sanity(self):
        """Get sanity check flag
        
        Returns
        -------
        boolean
            sanity check flag
        """        
        return self.engine.sanity_flag

    def get_data(self):
        """Get raw distribution data.
        
        Returns
        -------
        numpy 1D array
            raw distribution data
        """
        return np.array(self.engine.x)

    def get_plot_data(self):
        """Get raw distribution data and corrispective I_linspace
        
        Returns
        -------
        (numpy 1D array, numpy 1D array)
            (I_linspace, distribution data)
        """
        return (self.I, np.array(self.engine.x))

    def get_sum(self):
        """Get integral of the distribution (i.e. number of particles)
        
        Returns
        -------
        float
            Number of particles
        """
        return integrate.trapz(self.engine.x, x=self.I)

    def get_particle_loss(self):
        """Get amount of particle loss (when compared to starting condition)
        
        Returns
        -------
        float
            Particle loss quota
        """
        return -(
            integrate.trapz(self.get_data(), x=self.I) -
            integrate.trapz(self.I0, x=self.I)
        )

    def current(self, samples=5000, it_per_sample=20, disable_tqdm=True):
        """Perform automatic iteration of the simulation 
        and compute resulting current.
        
        Parameters
        ----------
        samples : int, optional
            number of current samples, by default 5000
        it_per_sample : int, optional
            number of sim. iterations per current sample, by default 20
        
        Returns
        -------
        (numpy 1D array, numpy 1D array)
            (times of the samples, current values for those samples)
        """
        current_array = np.empty(samples)
        temp1 = self.get_sum()
        times = (np.arange(samples) * it_per_sample +
                 self.engine.executed_iterations) * self.dt
        for i in tqdm(range(samples), disable=disable_tqdm):
            self.engine.iterate(it_per_sample)
            temp2 = self.get_sum()
            current_array[i] = (temp1 - temp2) / self.dt
            temp1 = temp2
        return times, current_array


class cn_double_polynomial(object):
    def __init__(self, I_max, c, exponent1, exponent2, I0, dt, normalize=True, I_min=0.0, I_star=1.0):
        self.I_max = I_max
        self.I_min = I_min
        self.c = c
        self.exponent1 = exponent1
        self.exponent2 = exponent2
        self.I0 = I0

        self.dt = dt
        self.samples = len(I0)

        self.I = np.linspace(I_min, I_max, self.samples)
        self.I_star = I_star
        self.dI = np.absolute(self.I[1] - self.I[0])
        self.half_dI = self.dI * 0.5

        self.locked_left = False
        self.locked_right = False

        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, I_star)) if \
                (i - self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        # For Reference:
        self.diffusion = self.poly_D(self.I, I_star)

        # Normalize?
        if normalize:
            self.I0 /= integrate.trapz(self.I0, x=self.I)

        self.engine = crank_nicolson(
            self.samples, I_min, I_max, self.dt, self.I0.copy(), A, B, C, D)

    def poly_D(self, I, I_star=1.0):
        return self.c * (np.power(I, self.exponent1) + I_star * (np.power(I, self.exponent2)))

    def set_source(self, source):
        """Apply a source vector to the simulation, this will overwrite all non zero values over the simulation distribution at each iteration.
        
        Parameters
        ----------
        source : ndarray
            source to apply
        """
        self.engine.set_source(source)

    def remove_source(self):
        """Remove the source vector to the simulation.
        """
        self.engine.remove_source()

    def lock_left(self):
        """Lock the left boundary to the non-zero value it has right now.
        """
        self.engine.set_lock_left()
        self.locked_left = True

    def lock_right(self):
        """Lock the right boundary to the non-zero value it has right now.
        """
        self.engine.set_lock_right()
        self.locked_right = True

    def unlock_left(self):
        """Unlock the left boundary and set it to zero.
        """
        self.engine.unlock_left()
        self.locked_left = False

    def unlock_right(self):
        """Unlock the right boundary and set it to zero.
        """
        self.engine.unlock_right()
        self.locked_right = False

    def extend(self, I_max):
        """Extends the size of the simulation and moves forward the absorbing
        barrier.
        
        Parameters
        ----------
        I_max : float
            new position for absorbing barrier
        """
        assert self.I_max < I_max
        extension = np.arange(self.I_max, I_max, self.dI)[1:]
        extension = np.append(extension, extension[-1] + self.dI)

        self.I = np.append(self.I, extension)
        self.I_max = self.I[-1]

        increasing = len(self.I) - self.samples
        self.samples = len(self.I)

        self.I0 = np.append(self.I0, np.zeros(increasing))
        data = np.append(np.array(self.engine.x), np.zeros(increasing))
        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, self.I_star)) if (i -
                                                                     self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, self.I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        N = self.engine.executed_iterations
        self.engine = crank_nicolson(
            self.samples, self.I_min, self.I[-1], self.dt, data, A, B, C, D)
        if self.locked_left:
            self.engine.set_lock_left()
        if self.locked_right:
            self.engine.set_lock_right()

        self.engine.set_executed_iterations(N)

        self.diffusion = self.poly_D(self.I, self.I_star)

    def cut(self, damping_point, length, I_max=-1.0):
        """Executes a damping of the distribution and, if required, reduces
        the size of the simulation.
        
        Parameters
        ----------
        damping_point : float
            point of damping
        length : float
            lenght of the damping
        I_max : float, optional
            new position for the absorbing barrier, by default -1.0
        """
        assert self.I_max > I_max
        assert self.I_max > damping_point

        # Logistic damping at given point
        new_data = logistic_damping(
            self.I, self.engine.x, damping_point, length)

        # Are we moving the collimator?
        if I_max != -1.0:
            assert damping_point <= I_max
            new_I = np.arange(self.I_min, I_max, self.dI)
            new_I = np.append(new_I, new_I[-1] + self.dI)

            self.I = new_I
            self.I_max = self.I[-1]

            self.I0 = self.I0[:len(self.I)]
            self.samples = len(self.I)
            new_data = new_data[:len(self.I)]

        # Let's make everything again
        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, self.I_star)) if (i -
                                                                     self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, self.I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        N = self.engine.executed_iterations
        self.engine = crank_nicolson(
            self.samples, self.I[0], self.I[-1], self.dt, new_data, A, B, C, D)
        if self.locked_left:
            self.engine.set_lock_left()
        if self.locked_right:
            self.engine.set_lock_right()

        self.engine.set_executed_iterations(N)

        self.diffusion = self.poly_D(self.I, self.I_star)

    def change_dt(self, new_dt):
        """Change the dt of the integrator.
        
        Parameters
        ----------
        new_dt : float
            New value for dt
        """
        data = np.array(self.engine.x)
        self.dt = new_dt

        A = []
        for i in self.I:
            A.append(self.poly_D(i - self.half_dI, self.I_star)) if (i -
                                                                     self.half_dI > 0) else A.append(0.0)
            A.append(self.poly_D(i + self.half_dI, self.I_star))
        A = np.array(A)
        B = np.zeros(self.samples)
        C = np.zeros(self.samples)
        D = np.zeros(self.samples + 2)

        N = self.engine.executed_iterations
        self.engine = crank_nicolson(
            self.samples, self.I[0], self.I[-1], self.dt, data, A, B, C, D)
        if self.locked_left:
            self.engine.set_lock_left()
        if self.locked_right:
            self.engine.set_lock_right()

        self.engine.set_executed_iterations(N)

    def iterate(self, n_iterations):
        """Iterates the simulation.
        
        Parameters
        ----------
        n_iterations : int
            number of iterations to perform
        """
        self.engine.iterate(n_iterations)

    def reset(self):
        """Resets the simulation to the starting condition.
        """
        self.engine.reset()

    def get_sanity(self):
        """Get sanity check flag
        
        Returns
        -------
        boolean
            sanity check flag
        """
        return self.engine.sanity_flag

    def get_data(self):
        """Get raw distribution data.
        
        Returns
        -------
        numpy 1D array
            raw distribution data
        """
        return np.array(self.engine.x)

    def get_plot_data(self):
        """Get raw distribution data and corrispective I_linspace
        
        Returns
        -------
        (numpy 1D array, numpy 1D array)
            (I_linspace, distribution data)
        """
        return (self.I, np.array(self.engine.x))

    def get_sum(self):
        """Get integral of the distribution (i.e. number of particles)
        
        Returns
        -------
        float
            Number of particles
        """
        return integrate.trapz(self.engine.x, x=self.I)

    def get_particle_loss(self):
        """Get amount of particle loss (when compared to starting condition)
        
        Returns
        -------
        float
            Particle loss quota
        """
        return -(
            integrate.trapz(self.get_data(), x=self.I) -
            integrate.trapz(self.I0, x=self.I)
        )

    def current(self, samples=5000, it_per_sample=20, disable_tqdm=True):
        """Perform automatic iteration of the simulation 
        and compute resulting current.
        
        Parameters
        ----------
        samples : int, optional
            number of current samples, by default 5000
        it_per_sample : int, optional
            number of sim. iterations per current sample, by default 20
        
        Returns
        -------
        (numpy 1D array, numpy 1D array)
            (times of the samples, current values for those samples)
        """
        current_array = np.empty(samples)
        temp1 = self.get_sum()
        times = (np.arange(samples) * it_per_sample +
                 self.engine.executed_iterations) * self.dt
        for i in tqdm(range(samples), disable=disable_tqdm):
            self.engine.iterate(it_per_sample)
            temp2 = self.get_sum()
            current_array[i] = (temp1 - temp2) / self.dt
            temp1 = temp2
        return times, current_array
