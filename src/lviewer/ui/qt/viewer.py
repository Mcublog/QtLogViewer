from dataclasses import dataclass, field

from PyQt6.QtCore import QObject

from lviewer.ui.qt.main.main_window import MainWindowUi
from lviewer.version import VERSION

MAIN_TITLE = f"LViewer v{VERSION}"


@dataclass(slots=True)
class QtApplicationView(QObject):

    ui: MainWindowUi = field(init=False)
    # error_message_signal = pyqtSignal(str, str)
    # info_message_signal = pyqtSignal(str, str)
    # changed_test_process_signal = pyqtSignal(TestProcessState)

    def __init__(self):
        super(QObject, self).__init__()

    def init(self, *args, **kwargs):
        self.ui = MainWindowUi(MAIN_TITLE)
        # self.error_message_signal.connect(self.ui.error_message)
        # self.info_message_signal.connect(self.ui.info_message)
        # self.changed_test_process_signal.connect(self.ui.changed_test_process)

    # def assign_callbacks(self,
    #                      main_window_callbacks: MainWindowUiCallbacks) -> None:
    #     self.ui.assign_callbacks(main_window_callbacks)

    # def port_list_update(self, portlist: list[str]) -> None:
    #     self.ui.port_list_update(portlist)

    # def get_selected_port(self, channel: int) -> str:
    #     return self.ui.get_selected_port(channel)

    # def set_connection_state(self, channel: int,
    #                          state: ConnectionState) -> None:
    #     self.ui.set_connection_state(channel, state)

    # def get_connection_state(self, channel: int) -> ConnectionState:
    #     return self.ui.get_connection_state(channel)

    # def set_channel_serial(self, channel: int, serial: str) -> None:
    #     self.ui.set_channel_serial(channel, serial)

    # def set_channel_fw_version(self, channel: int, version: str) -> None:
    #     self.ui.set_channel_fw_version(channel, version)

    # def set_statistic(self, channel: int, statistic: Statistic) -> None:
    #     self.ui.set_statistic(channel, statistic)

    # def set_test_process_state(self, state: TestProcessState) -> None:
    #     self.changed_test_process_signal.emit(state)

    # def set_channel_state(self, channel: int, state: ChannelState,
    #                       idle_states: list[ChannelIdleStates]) -> None:
    #     self.ui.set_channel_state(channel, state, idle_states)

    # def set_current_parameters(self, channel: int,
    #                            parameters: CurrentParameters) -> None:
    #     self.ui.set_current_parameters(channel, parameters)

    # def set_start_timestamp(self, start_timestamp: int) -> None:
    #     self.ui.set_start_timestamp(start_timestamp)

    def show(self) -> None:
        self.ui.show()

    # def request_test_type(self) -> ResourceTestCase:
    #     return self.ui.get_resource_test_case()

    def exit(self):
        self.ui.exit()

    # def error_message(self, title: str, msg: str) -> None:
    #     self.error_message_signal.emit(title, msg)

    # def info_message(self, title: str, msg: str) -> None:
    #     self.info_message_signal.emit(title, msg)

    # def set_cutter_mode(self, channel: int, mode: bool) -> None:
    #     self.ui.set_cutter_mode(channel, mode)

    # def set_cutter_value(self, channel: int, value: int) -> None:
    #     self.ui.set_cutter_value(channel, value)

    # def get_cutter_value(self, channel: int) -> int:
    #     return self.ui.get_cutter_value(channel)

    # def set_line_feed_value(self, channel: int, value: int) -> None:
    #     self.ui.set_line_feed_value(channel, value)
