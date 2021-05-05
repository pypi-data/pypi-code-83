
import numpy as np


class Model:
    def __init__(self, tap_initial=0, tap_min=-2, tap_max=2, activation_period_steps=0, blocking_period_steps=0,
                 p_reference_points_w=[0],
                 p_dependent_lower_limit_perunit=[0.97], p_dependent_upper_limit_perunit=[1.03]):
        self.tap_pos = int(round(tap_initial))
        self.tap_min = int(round(tap_min))
        self.tap_max = int(round(tap_max))
        self.activation_period_steps = int(round(activation_period_steps))
        self.blocking_period_steps = int(round(blocking_period_steps))
        self.time_until_blocked = 0
        self.continuous_activation_decrease_steps = 0
        self.continuous_activation_increase_steps = 0
        if not isinstance(p_reference_points_w, list):
            p_reference_points_w = [p_reference_points_w]
        if np.any(np.diff(p_reference_points_w) < 0):
            raise ValueError('Data points within parameter "p_reference_points_w" must be increasing')
        self.p_reference_points_w = p_reference_points_w
        if not isinstance(p_dependent_lower_limit_perunit, list):
            p_dependent_lower_limit_perunit = [p_dependent_lower_limit_perunit]
        self.p_dependent_lower_limit_perunit = p_dependent_lower_limit_perunit
        if not isinstance(p_dependent_upper_limit_perunit, list):
            p_dependent_upper_limit_perunit = [p_dependent_upper_limit_perunit]
        self.p_dependent_upper_limit_perunit = p_dependent_upper_limit_perunit

    def step(self, time, elapsed_time, volt_magnitude_perunit_controlled_node, p_reference_w=None):
        if self.time_until_blocked > time:
            return
        if p_reference_w is None:
            p_reference_w = self.p_reference_points_w[0]
        lower_limit_perunit, upper_limit_perunit = self.interp_power_dependent_limits(p_reference_w)
        if self.identify_decrease_activation(volt_magnitude_perunit_controlled_node, lower_limit_perunit, elapsed_time):
            self.try_decrease(time)
        elif self.identify_increase_activation(volt_magnitude_perunit_controlled_node,
                                               upper_limit_perunit, elapsed_time):
            self.try_increase(time)

    def interp_power_dependent_limits(self, p_reference_w):
        lower_limit_perunit = np.interp(p_reference_w, self.p_reference_points_w, self.p_dependent_lower_limit_perunit)
        upper_limit_perunit = np.interp(p_reference_w, self.p_reference_points_w, self.p_dependent_upper_limit_perunit)
        return lower_limit_perunit, upper_limit_perunit

    def identify_decrease_activation(self, volt_magnitude_perunit_controlled_node, lower_limit_perunit, elapsed_time):
        if volt_magnitude_perunit_controlled_node < lower_limit_perunit:
            self.reset_continuous_activation_increase()
            if self.continuous_activation_decrease_steps >= self.activation_period_steps:
                return True
            else:
                self.continuous_activation_decrease_steps += elapsed_time
        else:
            self.reset_continuous_activation_decrease()
        return False

    def identify_increase_activation(self, volt_magnitude_perunit_controlled_node, upper_limit_perunit, elapsed_time):
        if volt_magnitude_perunit_controlled_node > upper_limit_perunit:
            self.reset_continuous_activation_decrease()
            if self.continuous_activation_increase_steps >= self.activation_period_steps:
                return True
            else:
                self.continuous_activation_increase_steps += elapsed_time
        else:
            self.reset_continuous_activation_increase()
        return False

    def try_decrease(self, time):
        if self.tap_pos > self.tap_min:
            self.tap_pos -= 1
            self.reset_continuous_activation_decrease()
            self.activate_blocking_period(time)

    def try_increase(self, time):
        if self.tap_pos < self.tap_max:
            self.tap_pos += 1
            self.reset_continuous_activation_increase()
            self.activate_blocking_period(time)

    def activate_blocking_period(self, time):
        self.time_until_blocked = time + self.blocking_period_steps

    def reset_continuous_activation_decrease(self):
        self.continuous_activation_decrease_steps = 0

    def reset_continuous_activation_increase(self):
        self.continuous_activation_increase_steps = 0


if __name__ == '__main__':
    # This is how the tap controller can be used:
    tapCon = Model(tap_initial=0, tap_min=-2, tap_max=2, activation_period_steps=0, blocking_period_steps=0,
                   p_reference_points_w=[-200000, 0], p_dependent_lower_limit_perunit=[0.9, 1.06],
                   p_dependent_upper_limit_perunit=[0.93, 1.09])
    print('Initial tap position: %d' % tapCon.tap_pos)
    tapCon.step(time=10, elapsed_time=5, volt_magnitude_perunit_controlled_node=1.04, p_reference_w=200000)
    print('Tap position after control step: %d' % tapCon.tap_pos)
