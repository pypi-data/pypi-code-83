
import mosaik_api
from mosaik_gridcontrollers.TransformerTapControlSingleNode import Model
import logging

logger = logging.getLogger('TransformerTapControlSingleNode')

meta = {
    'models': {
        'TapControlModel': {
            'public': True,
            'params': ['tap_initial',
                       'tap_min',
                       'tap_max',
                       'activation_period_steps',
                       'blocking_period_steps',
                       'p_reference_points_w',
                       'p_dependent_lower_limit_perunit',
                       'p_dependent_upper_limit_perunit'
                       ],
            'attrs': ['volt_magnitude_perunit_controlled_node',
                      'p_reference_w',
                      'tap_setpoint'
                      ],
        },
    },
}


class Simulator(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(meta)
        self.eid_prefix = 'TapControl_'
        self.time_previous_step = 0
        self._controller_models = []
        self.entities = {}  # Maps EIDs to model indices in self._controller_models

    def init(self, sid, step_size=60):
        self.sid = sid
        self.step_size = step_size
        return self.meta

    def create(self, num, model, **model_params):
        next_eid = len(self.entities)
        entities = []
        for i in range(next_eid, next_eid + num):
            eid = '%s%d' % (self.eid_prefix, i)
            self.entities[eid] = i
            new_model = Model.Model(**model_params)
            self._controller_models.append(new_model)
            entities.append({'eid': eid, 'type': model})
            logger.info('Creating controller %s with parameters "%s"' % (eid, model_params))
        return entities

    def step(self, time, inputs):
        elapsed_time = time-self.time_previous_step
        for eid, attrs in inputs.items():
            model_idx = self.entities[eid]
            volt_magnitude_perunit = 1
            p_reference_w = None
            for attr, value in attrs.items():
                if attr == 'volt_magnitude_perunit_controlled_node':
                    volt_magnitude_perunit = list(value.values())[0]
                elif attr == 'p_reference_w':
                    p_reference_w = list(value.values())[0]
            self._controller_models[model_idx].step(time, elapsed_time, volt_magnitude_perunit, p_reference_w)
        self.time_previous_step = time
        return time + self.step_size

    def get_data(self, outputs):
        data = {}
        for eid, attrs in outputs.items():
            model_idx = self.entities[eid]
            data[eid] = {}
            for attr in attrs:
                if attr == 'tap_setpoint':
                    data[eid][attr] = self._controller_models[model_idx].tap_pos
                else:
                    raise ValueError('Unknown output attribute: %s' % attr)
        return data


def main():
    return mosaik_api.start_simulation(Simulator(), 'Transformator tap controller')


if __name__ == '__main__':
    main()
