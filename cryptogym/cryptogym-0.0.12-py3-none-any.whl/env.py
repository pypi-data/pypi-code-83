import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from gym import spaces
import matplotlib.pyplot as plt


class cryptoEnv(object):
    r"""A trading currency env that works in similar fashion to OpenAI gym
    Sends a state at time (t) at every step (minute/hour/day/week)
        ---> CSV must be set in latest-oldest prices
    Args:
        dataset: CSV dataset with OHLC (Open, High, Low, Close) prices
        available_cash: Amount of money that can be used to trade
        n_actions: Number of availabe actions
        loss_limit: Stops when wallets losses X amount of money 
            --> Start with $1000, stop when there is less than $700 total
                set loss_limit to 0.7
        n_actions: Sets the number of buy and sell actions
        loss_limit: Sets done flag when agent loses X amount of money.
        SEED: numpy random seed
    Shape (State):
        Prices are scaled.
        [Open, High, Low, Close, Cypto Wallet, USD_Wallet]
    Examples:
      --  s = env.reset()
      --   done = False
      --  while not done:
      --      action = agent.pick_action(s)
      --      s' , reward, done, info = env.step(action)
      --      s= s'
    """
    def __init__(self,
                 dataset,
                 available_cash,
                 n_actions=10,
                 loss_limit=0.7,
                 SEED=1337):
        np.random.seed(SEED)
        self.loss_limit = loss_limit
        self.scaler = StandardScaler()
        self.dataset = dataset
        self.price: float = None
        self.available_cash = available_cash
        self.usd_wallet: float = None
        self.crypto_wallet: float = None
        self.reward_dec: float = 1.0
        self.time_step: int = 0
        self.OHLC_shape = None
        self.scaled_stock_prices = None
        self.n_steps = None
        self.action_set = np.arange(-n_actions, n_actions)
        self.action_space = spaces.Discrete(len(self.action_set))
        self.obs_space = None
        self.portfolio, self.price_history = [], []
        self.scaled_prices = None
        self.OHLC_unscaled = self._load()
        self.episode = 0

    def _load(self):
        df = pd.read_csv(self.dataset)
        df = df.iloc[::-1]
        df = df.dropna()
        OHLC_prices = df.values
        self.scaled_prices = self.scaler.fit_transform(df)
        self.n_steps, self.OHLC_shape = OHLC_prices.shape
        # OHLC + Crypto Wallet + USD Wallet
        self.obs_space = np.empty(self.OHLC_shape + 2, dtype=np.float)
        return OHLC_prices

    def save_records(self):
        if not os.path.exists('history'):
            os.mkdir('history')
        plt.title("Price History")
        plt.xlabel("Time Steps")
        plt.ylabel("Price $(USD)")
        plt.plot(self.portfolio, label='Portfolio Total Balance')
        plt.plot(self.price_history, label='price')
        plt.legend()
        plt.savefig(f'history/episode_{self.episode}')
        plt.show()
        plt.clf()
        self.episode += 1

    def reset(self):
        self.portfolio, self.price_history = [], []
        self.time_step = 0
        self.crypto_wallet = 0
        self.usd_wallet = self.available_cash
        self._get_price()
        self.reward_dec -= 1e-3 if self.reward_dec > 0 else 0
        return self._get_obs()

    def step(self, a):
        assert (0 <= a <= len(self.action_set)), "Invalid Action"
        self.portfolio.append(self.usd_wallet + self.crypto_wallet)
        self.price_history.append(self.price)
        reward = 0.0
        prev_holding = self._get_holdings()
        self._trade(a)
        self.time_step += 1
        self._update_wallets()
        cur_holdings = self._get_holdings()

        profit = cur_holdings / prev_holding

        if cur_holdings < self.loss_limit * self.available_cash:
            done = True
        else:
            reward += 1
            done = (self.time_step == self.n_steps - 5)

        INFO = {"HOLDINGS": cur_holdings, "PROFIT": profit}

        if profit > 1.0:
            reward += (profit * self.reward_dec) + 1
        else:
            reward += (profit * self.reward_dec) - 1

        obs_ = self._get_obs()
        return obs_, reward, done, INFO

    def _get_holdings(self):
        return self.crypto_wallet + self.usd_wallet

    def _get_obs(self):
        self.obs_space[:4] = self.scaled_prices[self.time_step]
        self.obs_space[4] = self.crypto_wallet
        self.obs_space[5] = self.usd_wallet
        return self.obs_space

    def _trade(self, a):
        a -= 10
        a *= self.price
        if a < 0:
            self._buy_or_sell(a, purchase=False)
        elif a > 0:
            self._buy_or_sell(a, purchase=True)
        elif a == 0:
            return
        else:
            print("Not a valid action")
            return

    def _buy_or_sell(self, amount, purchase):
        amount = abs(amount)
        if purchase:
            if self.usd_wallet <= 0:
                return
            if self.usd_wallet >= amount:
                self.usd_wallet -= amount
                self.crypto_wallet += amount
        else:
            if self.crypto_wallet <= 0:
                return
            if self.crypto_wallet >= amount:
                self.crypto_wallet -= amount
                self.usd_wallet += amount

    def _get_price(self):
        self.price = self.OHLC_unscaled[self.time_step][3]

    def _update_wallets(self):
        self.crypto_wallet *= (self.OHLC_unscaled[self.time_step + 1][3] /
                               self.price)
