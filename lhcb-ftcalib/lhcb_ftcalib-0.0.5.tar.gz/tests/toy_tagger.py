import numpy as np
import pandas as pd
from tqdm import tqdm
import lhcb_ftcalib as ft
import matplotlib.pyplot as plt


def distribution_mistag(N, dist="normal"):
    if dist == "normal":
        return np.clip(np.random.normal(loc=0.3, scale=0.02, size=N), 0, 0.5)


def generate(N, calib, params, osc=True, DM=0.5065, DG=0, tau=1.52, Aprod=0):
    # Decay time and detector acceptance
    tau = np.random.exponential(scale = 1.0 / tau, size=N)
    tau_choose  = np.random.uniform(0, 1, N)
    tau = tau[tau_choose < 2 * np.arctan(2 * tau) / np.pi]

    N = len(tau)

    # Generate ETA and DEC randomly
    toydata = pd.DataFrame({
        "TAU" : tau,
        "ETA" : distribution_mistag(N),
        "DEC" : np.ones(N, dtype=np.int32)
    })
    toydata.DEC.loc[N // 2:] *= -1
    average_mistag = np.mean(toydata.ETA)

    # Compute true omega
    toydata["OMEGA"] = calib.eval(params, toydata.ETA, toydata.DEC, average_mistag)  # Ignore underflow, might cause a crash

    # Reconstruct true production flavour given true omega and true DEC
    toydata.eval("PROD = DEC", inplace=True)
    rand_thresh = np.random.uniform(0, 1, N)
    toydata.loc[rand_thresh < toydata.OMEGA, "PROD"] *= -1

    toydata.eval("DECAY = PROD", inplace=True)

    if osc:
        # Correct decay flavour for oscillation
        # Compute oscillation probability
        Amix = np.cos(DM * toydata.TAU) / np.cosh(0.5 * DG * toydata.TAU)
        osc_prob = 0.5 * (1 - Amix)
        rand_thresh = np.random.uniform(0, 1, N)

        # Flip decay flavour if oscillation is likely
        toydata.loc[rand_thresh < osc_prob, "DECAY"] *= -1
        # Tag correctness, i.e. ETA, OMEGA, DEC, PROD, stays the same

    # Shuffle
    toydata = toydata.sample(frac=1)

    return toydata


def calibrate(data):
    tagger = ft.Tagger("TOY", data.ETA, data.DEC, data.DECAY * 511, "Bd", tau_ps=data.TAU)
    tagger.calibrate()
    params, nom, unc, cov = tagger.get_fitparameters()

    return tagger.params_nominal, tagger.params_uncerts


def pull_plots(toy_noms, toy_uncs, truth):
    for p, truep in enumerate(truth):
        pull = (toy_noms[:, p] - truep)
        plt.subplot(2, 2, p + 1)
        plt.hist(pull, range=(-0.1, 0.1), histtype="stepfilled")

    plt.show()


if __name__ == "__main__":
    result_num = []
    result_unc = []

    truth = [0.02, 1.1, 0.03, 0.8]

    for i in tqdm(range(100)):
        data = generate(100000, ft.PolynomialCalibration(2, ft.link.mistag), [0.02, 1.1, 0.03, 0.8], True)
        nom, unc = calibrate(data)
        result_num.append(nom)
        result_unc.append(unc)

    result_num = np.array(result_num)
    result_unc = np.array(result_unc)
    print(result_num)
    print(result_unc)

    pull_plots(result_num, result_unc, truth)
