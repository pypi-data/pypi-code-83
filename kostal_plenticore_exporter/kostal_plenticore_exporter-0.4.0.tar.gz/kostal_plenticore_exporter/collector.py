import kostalplenticore
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily, InfoMetricFamily


class PlenticoreCollector:
    def __init__(self, ip: str, password: str):
        self.source = kostalplenticore.connect(ip, password)
        self.source.login()

    def _get_processdata(self, moduleid, processdata):
        try:
            return {result['id']: result['value'] for result in self.source.getProcessdata(moduleid, processdata)}
        except KeyError:
            # getProcessdata key errors if auth has expired (i.e. after restart). Try to fix it for the next scrape
            self.source.login()
            raise

    def _get_settings(self, moduleid, settingids):
        try:
            return {result['id']: result['value'] for result in self.source.getSettings(moduleid, settingids)}
        except KeyError:
            # getSettings key errors if auth has expired (i.e. after restart). Try to fix it for the next scrape
            self.source.login()
            raise

    def _info_metric(self):
        info = InfoMetricFamily('kostal_plenticore', 'Inverter metadata')
        info.add_metric([], self.source.getInfo())
        return info

    def _string_metrics(self):
        current = GaugeMetricFamily(
            'kostal_plenticore_string_current_amperes', 'Current current on the PV string', labels=['string']
        )
        power = GaugeMetricFamily(
            'kostal_plenticore_string_power_watts', 'Current power on the PV string', labels=['string']
        )
        voltage = GaugeMetricFamily(
            'kostal_plenticore_string_voltage_volts', 'Current voltage on the PV string', labels=['string']
        )

        for string in range(1, 3):
            string_data = self._get_processdata(f'devices:local:pv{string}', ['I', 'P', 'U'])
            current.add_metric([f'pv{string}'], string_data['I'])
            power.add_metric([f'pv{string}'], string_data['P'])
            voltage.add_metric([f'pv{string}'], string_data['U'])

        return current, power, voltage

    def _battery_metrics(self):
        battery_data = self._get_processdata('devices:local:battery', [
            'BatManufacturer', 'BatModel', 'BatVersionFW', 'Cycles', 'SoC'
        ])

        cycles = GaugeMetricFamily('kostal_plenticore_battery_cycles_total', "Battery cycle count")
        cycles.add_metric([], battery_data['Cycles'])

        charge = GaugeMetricFamily('kostal_plenticore_battery_charge_percent', "Battery charge in percent")
        charge.add_metric([], battery_data['SoC'])

        min_charge = GaugeMetricFamily(
            'kostal_plenticore_battery_configured_minimum_charge_percent',
            "The minumum charge target in percent configured for the Battery")
        min_charge.add_metric([], self._get_settings('devices:local', ['Battery:MinSoc'])['Battery:MinSoc'])

        return cycles, charge, min_charge

    def _event_metrics(self):
        event_data = self._get_processdata('scb:event', ['Event:ActiveErrorCnt', 'Event:ActiveWarningCnt'])

        events = GaugeMetricFamily('kostal_plenticore_active_events_total', "Active events", labels=['severity'])
        events.add_metric(["error"], event_data['Event:ActiveErrorCnt'])
        events.add_metric(["warning"], event_data['Event:ActiveWarningCnt'])

        return events

    def _energy_metrics(self):
        energy_flows = [
            'ChargeGrid', 'ChargeInvIn', 'ChargePv', 'Discharge', 'DischargeGrid',
            'Home', 'HomeBat', 'HomeGrid', 'HomeOwn', 'HomePv',
            'Pv1', 'Pv2', 'Pv3',
        ]

        energy_data = self._get_processdata('scb:statistic:EnergyFlow', [
            f'Statistic:Energy{flow}:Total' for flow in energy_flows
        ] + ['Statistic:Yield:Total'])

        metric = CounterMetricFamily(
            'kostal_plenticore_energy_flow_watt_hours', 'Total energy flows in watt hours', labels=['flow']
        )
        for flow in energy_flows:
            metric.add_metric([flow], energy_data[f'Statistic:Energy{flow}:Total'])
        metric.add_metric(['Yield'], energy_data['Statistic:Yield:Total'])
        return metric

    def _update_metrics(self):
        update_data = self._get_processdata('scb:update', [
            'Update:Status',  # 2.0 if update available
            'Update:StatusTime',
        ])
        status_metric = GaugeMetricFamily(
            'kostal_plenticore_update_status',
            'Software update status of the inverter. 2.0 if update is available.'
        )
        status_metric.add_metric([], update_data['Update:Status'])
        status_time_metric = GaugeMetricFamily(
            'kostal_plenticore_update_status_timestamp',
            'Unix time when current update status was established.'
        )
        status_time_metric.add_metric([], update_data['Update:StatusTime'])
        return status_metric, status_time_metric

    def collect(self):
        yield self._info_metric()
        for metric in self._string_metrics():
            yield metric
        for metric in self._battery_metrics():
            yield metric
        yield self._event_metrics()
        yield self._energy_metrics()
        for metric in self._update_metrics():
            yield metric
