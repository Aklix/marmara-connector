from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QFontDatabase, QFont
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from qtguidesign import Ui_MainWindow
from PyQt5.uic import loadUi
import qtawesome as qta
import configuration

icon_path = ApplicationContext().get_resource("images")
style_path = ApplicationContext().get_resource("styles")


class GuiStyle(Ui_MainWindow):

    def __init__(self):
        # loadUi("qtguidesign.ui", self)  #  loadin from qtguidesign.ui
        self.setupUi(self)  # loading from qtguidesign.py
        # setting params
        self.icon_path = icon_path
        logo = QPixmap(self.icon_path + '/mcl_logo.png')
        self.logo_label.setPixmap(logo)
        # Chain page
        self.stopchain_button.setIcon(QtGui.QIcon(self.icon_path + "/stop_icon.png"))
        self.stopchain_button.setIconSize(QtCore.QSize(32, 32))
        # Side panel
        self.inactive_icon_pixmap = QPixmap(self.icon_path + '/circle-inactive.png')
        self.active_icon_pixmap = QPixmap(self.icon_path + '/circle-active.png')
        self.chainstatus_label_value.setPixmap(self.inactive_icon_pixmap)
        self.chainsync_label_value.setPixmap(self.inactive_icon_pixmap)
        self.coffee_pixmap = QPixmap(self.icon_path + '/Coffee-icon.png')
        self.coffee_icon_label.setPixmap(self.coffee_pixmap)
        self.staking_button.setVisible(False)
        self.staking_button = ToggleSwitch(self.miningstatus_frame)
        self.staking_button.setObjectName("staking_button")
        self.gridLayout_17.addWidget(self.staking_button, 1, 1, 1, 1)
        self.mining_button.setVisible(False)
        self.mining_button = ToggleSwitch(self.miningstatus_frame)
        self.mining_button.setObjectName("mining_button")
        self.support_pushButton.setText('Support')
        self.support_pushButton.setEnabled(False)
        self.connections_warning_label.setPixmap(QPixmap(self.icon_path + '/warning-icon.png'))
        self.connections_warning_label.setVisible(True)
        # Stats
        self.gridLayout_17.addWidget(self.mining_button, 3, 1, 1, 1)
        self.stats_pie_frame.setContentsMargins(0, 0, 0, 0)
        self.stats_layout = QtWidgets.QHBoxLayout(self.stats_pie_frame)
        self.stats_layout.setContentsMargins(0, 0, 0, 0)
        # Market
        self.exchange_pixmap = QPixmap(self.icon_path + '/arrow-double-icon.png')
        self.exchange_label_icon.setPixmap(self.exchange_pixmap)
        # self.set_icon_color('black')

    def set_icon_color(self, color):
        # Chain page
        self.download_blocks_button.setIcon(qta.icon('mdi.cloud-download-outline', color=color))
        self.download_blocks_button.setIconSize(QtCore.QSize(24, 24))
        self.refresh_walletaddresses_button.setIcon(qta.icon('mdi.refresh', color=color))
        self.refresh_walletaddresses_button.setIconSize(QtCore.QSize(24, 24))
        self.check_fork_button.setIcon(qta.icon('mdi.directions-fork', color=color))
        self.check_fork_button.setIconSize(QtCore.QSize(24, 24))
        self.addaddress_page_button.setIcon(qta.icon('fa.plus', color=color))
        self.addaddress_page_button.setIconSize(QtCore.QSize(24, 24))
        self.address_seed_button.setIcon(qta.icon('mdi.seed-outline', color=color))
        self.address_seed_button.setIconSize(QtCore.QSize(24, 24))
        self.newaddress_button.setIcon(qta.icon('mdi.credit-card-plus-outline', color=color))
        self.newaddress_button.setIconSize(QtCore.QSize(24, 24))
        self.addresspage_back_button.setIcon(qta.icon('mdi.step-backward', color=color))
        self.addresspage_back_button.setIconSize(QtCore.QSize(24, 24))
        self.privatekeypage_back_button.setIcon(qta.icon('mdi.step-backward', color=color))
        self.privatekeypage_back_button.setIconSize(QtCore.QSize(24, 24))
        self.importprivkey_button.setIcon(qta.icon('mdi.application-import', color=color))
        self.importprivkey_button.setIconSize(QtCore.QSize(24, 24))
        self.privkey_page_button.setIcon(qta.icon('mdi.incognito', color=color))
        self.privkey_page_button.setIconSize(QtCore.QSize(24, 24))
        # menubar
        self.actionQuit.setIcon(qta.icon('fa.close', color=color))
        self.actionLogout.setIcon(qta.icon('mdi.logout', color=color))
        self.menuDebug.setIcon(qta.icon('fa.bug', color=color))
        self.actionAbout.setIcon(qta.icon('fa.info', color=color))
        self.actionLanguage_Selection.setIcon(qta.icon('ei.flag', color=color))
        self.actionAppearances.setIcon(qta.icon('fa.paint-brush', color=color))
        self.actionSee_Log_File.setIcon(qta.icon('mdi.file-document-outline', color=color))
        self.actionCheck_for_Update.setIcon(qta.icon('mdi.open-in-app', color=color))
        # mcl tab
        self.mcl_tab.setTabIcon(0, qta.icon('fa.chain', color=color))
        self.mcl_tab.setTabIcon(1, qta.icon('fa5s.wallet', color=color))
        self.mcl_tab.setTabIcon(2, qta.icon('fa5s.coins', color=color))
        self.mcl_tab.setTabIcon(3, qta.icon('fa5b.hornbill', color=color))
        self.mcl_tab.setTabIcon(4, qta.icon('fa5.address-card', color=color))
        self.mcl_tab.setTabIcon(5, qta.icon("mdi.chart-areaspline", color=color))
        self.mcl_tab.setTabIcon(6, qta.icon("mdi.bulletin-board", color=color))
        self.mcl_tab.setIconSize(QtCore.QSize(28, 28))
        # Side panel
        self.getinfo_refresh_button.setIcon(qta.icon('ei.refresh', color=color))
        self.getinfo_refresh_button.setIconSize(QtCore.QSize(24, 24))
        self.copyaddress_button.setIcon(qta.icon('fa5.copy', color=color))
        self.copyaddress_button.setIconSize(QtCore.QSize(24, 24))
        self.copypubkey_button.setIcon(qta.icon('mdi.key-change', color=color))
        self.copypubkey_button.setIconSize(QtCore.QSize(24, 24))
        self.fontsize_minus_button.setIcon(qta.icon('mdi.format-font-size-decrease', color=color))
        self.fontsize_minus_button.setIconSize(QtCore.QSize(24, 24))
        self.fontsize_plus_button.setIcon(qta.icon('mdi.format-font-size-increase', color=color))
        self.fontsize_plus_button.setIconSize(QtCore.QSize(24, 24))
        # Wallet page button icons
        self.lock_button.setIcon(QtGui.QIcon(qta.icon('fa5s.lock', color=color)))
        self.lock_button.setIconSize(QtCore.QSize(32, 32))
        self.unlock_button.setIcon(QtGui.QIcon(qta.icon('fa5s.unlock-alt', color=color)))
        self.unlock_button.setIconSize(QtCore.QSize(32, 32))
        self.addressamount_refresh_button.setIcon(qta.icon('mdi.refresh', color=color))
        self.addressamount_refresh_button.setIconSize(QtCore.QSize(24, 24))
        self.refresh_loopinfo_button.setIcon(qta.icon('mdi.refresh', color=color))
        self.refresh_loopinfo_button.setIconSize(QtCore.QSize(24, 24))
        # Coin Send-Receive page
        self.coinsend_button.setIcon(qta.icon('mdi.database-export', color=color))
        self.coinsend_button.setIconSize(QtCore.QSize(24, 24))
        self.transaction_search_button.setIcon(qta.icon('fa.search', color=color))
        self.transaction_search_button.setIconSize(QtCore.QSize(24, 24))
        self.qrcode_button.setIcon(qta.icon('mdi.qrcode', color=color))
        self.qrcode_button.setIconSize(QtCore.QSize(48, 48))
        # Credit loops page
        self.creditloop_tabWidget.setTabIcon(0, qta.icon('mdi.arrow-down-circle-outline', color=color))
        self.creditloop_tabWidget.setTabIcon(1, qta.icon('mdi.link-variant-plus', color=color))
        self.creditloop_tabWidget.setTabIcon(2, qta.icon('mdi.vector-circle', color=color))
        self.creditloop_tabWidget.setTabIcon(3, qta.icon('mdi.database-search', color=color))
        self.creditloop_tabWidget.setIconSize(QtCore.QSize(24, 24))

        self.looprequest_search_button.setIcon(qta.icon('fa.search', color=color))
        self.looprequest_search_button.setIconSize(QtCore.QSize(24, 24))

        self.send_loop_request_button.setIcon(qta.icon('ei.share-alt', color=color))
        self.send_loop_request_button.setIconSize(QtCore.QSize(24, 24))
        self.send_transfer_request_button.setIcon(qta.icon('ei.share-alt', color=color))
        self.send_transfer_request_button.setIconSize(QtCore.QSize(24, 24))

        self.lq_pubkey_search_button.setIcon(qta.icon('fa.search', color=color))
        self.lq_pubkey_search_button.setIconSize(QtCore.QSize(24, 24))

        self.lq_txid_search_button.setIcon(qta.icon('fa.search', color=color))
        self.lq_txid_search_button.setIconSize(QtCore.QSize(24, 24))

        self.activeloops_search_button.setIcon(qta.icon('fa.search', color=color))
        self.activeloops_search_button.setIconSize(QtCore.QSize(24, 24))
        self.holderloops_search_button.setIcon(qta.icon('fa.search', color=color))
        self.holderloops_search_button.setIconSize(QtCore.QSize(24, 24))
        # Contacts page
        self.clear_contact_button.setIcon(qta.icon('ei.broom', color=color))
        self.clear_contact_button.setIconSize(QtCore.QSize(24, 24))
        self.addcontact_button.setIcon(qta.icon('fa.user-plus', color=color))
        self.addcontact_button.setIconSize(QtCore.QSize(24, 24))
        self.updatecontact_button.setIcon(qta.icon('fa5s.user-edit', color=color))
        self.updatecontact_button.setIconSize(QtCore.QSize(24, 24))
        self.deletecontact_button.setIcon(qta.icon('fa5s.user-slash', color=color))
        self.deletecontact_button.setIconSize(QtCore.QSize(24, 24))
        # Stats
        self.stats_refresh_pushButton.setIcon(qta.icon('mdi.refresh', color=color))
        self.stats_refresh_pushButton.setIconSize(QtCore.QSize(24, 24))
        self.stats_calculate_pushButton.setIcon(qta.icon('mdi.calculator-variant-outline', color=color))
        self.stats_calculate_pushButton.setIconSize(QtCore.QSize(24, 24))
        # Market
        self.exchange_market_request_button.setIcon(qta.icon('mdi.arrow-bottom-left-thick', color=color))
        self.exchange_market_request_button.setIconSize(QtCore.QSize(24, 24))

    def set_font_size(self, size):
        font = QFont()
        font.setPointSize(size)
        self.centralwidget.setFont(font)
        self.menuBar.setFont(font)
        # talbewidget fontsize
        self.addresses_tableWidget.setFont(font)
        self.addresses_tableWidget.horizontalHeader().setFont(font)
        self.addresses_privkey_tableWidget.setFont(font)
        self.addresses_privkey_tableWidget.horizontalHeader().setFont(font)
        self.transactions_tableWidget.setFont(font)
        self.transactions_tableWidget.horizontalHeader().setFont(font)
        self.loop_request_tableWidget.setFont(font)
        self.loop_request_tableWidget.horizontalHeader().setFont(font)
        self.transferrequests_tableWidget.setFont(font)
        self.transferrequests_tableWidget.horizontalHeader().setFont(font)
        self.activeloops_tableWidget.setFont(font)
        self.activeloops_tableWidget.horizontalHeader().setFont(font)
        self.transferableloops_tableWidget.setFont(font)
        self.transferableloops_tableWidget.horizontalHeader().setFont(font)
        self.contacts_tableWidget.setFont(font)
        self.contacts_tableWidget.horizontalHeader().setFont(font)
        self.exchange_market_tableWidget.setFont(font)
        self.exchange_market_tableWidget.horizontalHeader().setFont(font)
        # label Font size
        # login page labels
        self.local_button.setFont(font)
        self.remote_button.setFont(font)
        self.serveradd_button.setFont(font)
        self.serveredit_button.setFont(font)
        self.serverpw_lineEdit.setFont(font)
        self.remotelogin_label.setFont(font)
        self.connect_button.setFont(font)
        self.add_remotehost_label.setFont(font)
        self.add_serversave_button.setFont(font)
        self.servercancel_button.setFont(font)
        self.add_servername_label.setFont(font)
        self.add_servername_lineEdit.setFont(font)
        self.add_serverusername_label.setFont(font)
        self.add_serverusername_lineEdit.setFont(font)
        self.add_serverip_label.setFont(font)
        self.add_serverip_lineEdit.setFont(font)
        self.edit_serverip_lineEdit.setFont(font)
        self.edit_serverip_label.setFont(font)
        self.edit_serverusername_label.setFont(font)
        self.edit_servername_label.setFont(font)
        self.edit_serverusername_lineEdit.setFont(font)
        self.edit_servername_lineEdit.setFont(font)
        self.edit_serversave_button.setFont(font)
        self.serverdelete_button.setFont(font)
        self.edit_remotehost_label.setFont(font)
        self.home_button.setFont(font)
        self.server_comboBox.setFont(font)
        # Install Page
        self.sudo_password_lineEdit.setFont(font)
        self.start_install_button.setFont(font)
        self.install_progress_textBrowser.setFont(font)
        self.install_progressBar.setFont(font)
        # mcl page
        self.mcl_tab.tabBar().setFont(font)
        # Side panel Labels
        self.walletsummary_label.setFont(font)
        self.totalnormal_label.setFont(font)
        self.totalnormal_value_label.setFont(font)
        self.totalactivated_label.setFont(font)
        self.totalactivated_value_label.setFont(font)
        self.currentblock_label.setFont(font)
        self.currentblock_value_label.setFont(font)
        self.difficulty_label.setFont(font)
        self.difficulty_value_label.setFont(font)
        self.longestchain_label.setFont(font)
        self.longestchain_value_label.setFont(font)
        self.connections_label.setFont(font)
        self.connections_value_label.setFont(font)
        self.chainstatus_label.setFont(font)
        self.chainstatus_label_value.setFont(font)
        self.chainsync_label.setFont(font)
        self.chainsync_label_value.setFont(font)
        self.getinfo_refresh_button.setFont(font)
        self.staking_label.setFont(font)
        self.mining_label.setFont(font)
        self.cpu_label.setFont(font)
        self.cpu_core_lineEdit.setFont(font)
        self.cpu_core_set_button.setFont(font)
        self.miningstatus_label.setFont(font)
        self.support_pushButton.setFont(font)
        self.coffee_icon_label.setFont(font)
        self.multiply_label.setFont(font)
        self.cup_lineEdit.setFont(font)
        self.copypubkey_button.setFont(font)
        self.copyaddress_button.setFont(font)
        self.fontsize_minus_button.setFont(font)
        self.fontsize_plus_button.setFont(font)
        # Chain tab label
        self.chain_version_label.setFont(font)
        self.privkey_page_button.setFont(font)
        self.addaddress_page_button.setFont(font)
        self.chain_wallet_addresses_label.setFont(font)
        self.stopchain_button.setFont(font)
        self.hide_address_checkBox.setFont(font)
        self.download_blocks_button.setFont(font)
        self.check_fork_button.setFont(font)
        self.update_chain_button.setFont(font)
        self.newaddress_button.setFont(font)
        self.create_newaddress_label.setFont(font)
        self.address_seed_button.setFont(font)
        self.confirm_passphrase_TextEdit.setFont(font)
        self.create_seed_label.setFont(font)
        self.passphrase_TextEdit.setFont(font)
        self.addresspage_back_button.setFont(font)
        self.privatekeypage_back_button.setFont(font)
        self.see_address_privkeys_label.setFont(font)
        self.importprivkey_label.setFont(font)
        self.importprivkey_button.setFont(font)
        self.privkey_lineEdit.setFont(font)
        self.update_chain_textBrowser.setFont(font)
        # Wallet page label
        self.unlock_amount_label.setFont(font)
        self.unlock_amount_value.setFont(font)
        self.unlock_button.setFont(font)
        self.lock_amount_label.setFont(font)
        self.lock_amount_value.setFont(font)
        self.lock_button.setFont(font)
        self.unlock_activeamount_label.setFont(font)
        self.lock_normal_amount_label.setFont(font)
        self.normal_amount_label.setFont(font)
        self.normal_amount_value.setFont(font)
        self.wallet_total_activated_label.setFont(font)
        self.wallet_total_activated_value.setFont(font)
        self.wallet_balance_label.setFont(font)
        self.wallet_total_normal_label.setFont(font)
        self.wallet_total_normal_value.setFont(font)
        self.activated_amount_label.setFont(font)
        self.activated_amount_value.setFont(font)
        self.pubkey_balance_label.setFont(font)
        self.addressamount_refresh_button.setFont(font)
        self.currentpubkey_label.setFont(font)
        self.current_pubkey_value.setFont(font)
        self.currentaddress_label.setFont(font)
        self.currentaddress_value.setFont(font)
        self.refresh_loopinfo_button.setFont(font)
        # Coin send receive page
        self.transaction_startdate_label.setFont(font)
        self.transaction_enddate_label.setFont(font)
        self.transaction_search_button.setFont(font)
        self.transactions_label.setFont(font)
        self.coinreceive_label.setFont(font)
        self.receiver_address_lineEdit.setFont(font)
        self.sending_amount_label.setFont(font)
        self.sending_amount_lineEdit.setFont(font)
        self.coinsend_button.setFont(font)
        self.contacts_address_comboBox.setFont(font)
        self.receiver_address_label.setFont(font)
        self.coinsend_label.setFont(font)
        self.qrcode_button.setFont(font)
        self.transactions_startdate_dateTimeEdit.setFont(font)
        self.transactions_startdate_dateTimeEdit.calendarWidget().setFont(font)
        self.transactions_endtdate_dateTimeEdit.setFont(font)
        self.transactions_endtdate_dateTimeEdit.calendarWidget().setFont(font)
        # Creditloops page
        self.creditloop_tabWidget.tabBar().setFont(font)
        # Incoming loop request
        self.looprequest_search_button.setFont(font)
        self.requestdate_label.setFont(font)
        self.request_dateTimeEdit.setFont(font)
        self.request_dateTimeEdit.calendarWidget().setFont(font)
        self.request_date_checkBox.setFont(font)
        self.loop_request_label.setFont(font)
        self.transferrequests_label.setFont(font)
        # make loop request
        self.create_loop_request_label.setFont(font)
        self.send_loop_request_button.setFont(font)
        self.make_credit_loop_amount_label.setFont(font)
        self.make_credit_loop_amount_lineEdit.setFont(font)
        self.make_credit_loop_matures_label.setFont(font)
        self.make_credit_loop_matures_dateTimeEdit.setFont(font)
        self.make_credit_loop_matures_dateTimeEdit.calendarWidget().setFont(font)
        self.make_credit_loop_currency_label.setFont(font)
        self.make_credit_loop_currency_value_label.setFont(font)
        self.make_credit_loop_senderpubkey_label.setFont(font)
        self.make_credit_loop_senderpubkey_lineEdit.setFont(font)
        self.contactpk_makeloop_comboBox.setFont(font)
        self.create_transfer_request_label.setFont(font)
        self.transfer_senderpubkey_label.setFont(font)
        self.transfer_senderpubkey_lineEdit.setFont(font)
        self.send_transfer_request_button.setFont(font)
        self.transfer_baton_label.setFont(font)
        self.transfer_baton_lineEdit.setFont(font)
        self.contactpk_transferrequest_comboBox.setFont(font)
        self.total_issuer_loop_amount_label.setFont(font)

        # Active Loops
        self.Issuerloops_label.setFont(font)
        self.total_transferrable_loop_amount_label.setFont(font)
        self.total_transferrable_loop_amount_label_value.setFont(font)
        self.numberof_transferrable_loop_amount_label.setFont(font)
        self.numberof_transferrable_loop_amount_label_value.setFont(font)
        self.holderloops_closed_amount_label.setFont(font)
        self.holderloops_closed_amount_label_value.setFont(font)
        self.holderloops_closed_number_label.setFont(font)
        self.holderloops_closed_number_label_value.setFont(font)
        self.holderloops_search_button.setFont(font)
        self.transferableloops_label.setFont(font)
        self.activeloops_search_button.setFont(font)
        self.total_issuer_loop_amount_label_value.setFont(font)
        self.activeloops_pending_number_label.setFont(font)
        self.activeloops_pending_number_value_label.setFont(font)
        self.closedloops_total_amount_label.setFont(font)
        self.closedloops_total_amount_value_label.setFont(font)
        self.closedloops_total_number_label.setFont(font)
        self.closedloops_total_number_value_label.setFont(font)
        self.activeloops_total_amount_label.setFont(font)
        self.activeloops_total_amount_value_label.setFont(font)
        self.numberof_total_activeloops_label.setFont(font)
        self.numberof_total_activeloops_label_value.setFont(font)
        self.my_stats_normal_label.setFont(font)
        self.my_stats_normal_label_value.setFont(font)
        self.my_stats_activated_label.setFont(font)
        self.my_stats_activated_label_value.setFont(font)
        self.my_stats_inloops_label.setFont(font)
        self.my_stats_inloops_label_value.setFont(font)
        # Loop queries
        self.loopqueries_pubkey_label.setFont(font)
        self.loopqueries_pubkey_lineEdit.setFont(font)
        self.lq_pubkey_search_button.setFont(font)
        self.lq_pubkeynormalamount_label.setFont(font)
        self.lq_pubkeynormalamount_value_label.setFont(font)
        self.lq_pubkeyclosedloopamount_label.setFont(font)
        self.lq_pubkeyclosedloopamount_value_label.setFont(font)
        self.lq_activeloopno_label.setFont(font)
        self.lq_activeloopno_value_label.setFont(font)
        self.lq_pubkeyactivatedamount_label.setFont(font)
        self.lq_pubkeyactivatedamount_value_label.setFont(font)
        self.lq_closedloopno_label.setFont(font)
        self.lq_closedloopno_value_label.setFont(font)
        self.lq_pubkeyloopamount_label.setFont(font)
        self.lq_pubkeyloopamount_value_label.setFont(font)
        self.lq_pubkey_address_label.setFont(font)
        self.lq_pubkey_address_label_value.setFont(font)
        self.loopquery_transfercount_label.setFont(font)
        self.loopquery_transfercount_value.setFont(font)
        self.loopquery_matures_label.setFont(font)
        self.loopquery_matures_value.setFont(font)
        self.loopquery_currency_label.setFont(font)
        self.loopquery_currency_value.setFont(font)
        self.loopquery_amount_label.setFont(font)
        self.loopquery_amount_value.setFont(font)
        self.loopquery_issuer_label.setFont(font)
        self.loopquery_issuer_value.setFont(font)
        self.loopquery_baton_label.setFont(font)
        self.loopquery_baton_value.setFont(font)
        self.loopquery_batonpk_label.setFont(font)
        self.loopquery_batonpk_value.setFont(font)
        self.loopquery_info_label.setFont(font)
        self.loopsearch_txid_label.setFont(font)
        self.loopsearch_txid_lineEdit.setFont(font)
        self.lq_txid_search_button.setFont(font)
        # Contacts Page
        self.updatecontact_button.setFont(font)
        self.addcontact_button.setFont(font)
        self.contactname_label.setFont(font)
        self.contactname_lineEdit.setFont(font)
        self.contactaddress_label.setFont(font)
        self.contactaddress_lineEdit.setFont(font)
        self.contactpubkey_label.setFont(font)
        self.contactpubkey_lineEdit.setFont(font)
        self.contactgroup_lineEdit.setFont(font)
        self.contactgroup_label.setFont(font)
        self.deletecontact_button.setFont(font)
        self.clear_contact_button.setFont(font)
        # Stats Page
        self.stats_amount_in_activated_label.setFont(font)
        self.stats_amount_in_activated_lineEdit.setFont(font)
        self.stats_amount_in_loops_label.setFont(font)
        self.stats_amount_in_loops_lineEdit.setFont(font)
        self.stats_estimated_staking_label.setFont(font)
        self.stats_estimated_staking_label_value.setFont(font)
        self.stats_calculate_pushButton.setFont(font)
        self.stats_height_label.setFont(font)
        self.stats_height_value_label.setFont(font)
        self.stats_in_loops_label.setFont(font)
        self.stats_in_loops_label_value.setFont(font)
        self.stats_activated_label.setFont(font)
        self.stats_activated_label_value.setFont(font)
        self.stats_normal_label.setFont(font)
        self.stats_normal_label_value.setFont(font)
        self.stats_label.setFont(font)
        # Market Page
        self.usd_amount_lineEdit.setFont(font)
        self.convert_mcl_label.setFont(font)
        self.exchange_label_icon.setFont(font)
        self.mcl_amount_lineEdit.setFont(font)
        self.convert_usd_label.setFont(font)
        self.mcl_usd_calculator_label.setFont(font)
        self.exchange_market_label.setFont(font)
        self.ticker_volume_label.setFont(font)
        self.ticker_volume_label_value.setFont(font)
        self.ticker_1hour_label.setFont(font)
        self.ticker_1hour_label_value.setFont(font)
        self.ticker_1week_label.setFont(font)
        self.ticker_1week_label_value.setFont(font)
        self.ticker_price_label.setFont(font)
        self.ticker_price_label_value.setFont(font)
        self.ticker_24hour_label.setFont(font)
        self.ticker_24hour_label_value.setFont(font)
        self.ticker_1month_label.setFont(font)
        self.ticker_1month_label_value.setFont(font)
        self.exchange_market_comboBox.setFont(font)
        # header label fontsize
        font.setPointSize(size + 4)
        self.login_label.setFont(font)
        self.remotelogin_label.setFont(font)
        self.add_remotehost_label.setFont(font)
        self.edit_remotehost_label.setFont(font)
        # Menu items font
        font.setPointSize(size - 1)
        self.actionQuit.setFont(font)
        self.actionAbout.setFont(font)
        self.actionLogout.setFont(font)
        self.actionAppearances.setFont(font)
        self.actionConsole.setFont(font)
        self.actionCheck_for_Update.setFont(font)
        self.actionLanguage_Selection.setFont(font)
        self.menuHelp.setFont(font)
        self.actionSee_Log_File.setFont(font)
        # smaller fontsize
        font.setPointSize(size-2)
        self.login_message_label.setFont(font)
        self.bottom_message_label.setFont(font)
        self.last_update_label.setFont(font)
        self.mining_button.setFont(font)
        self.staking_button.setFont(font)
        # set config fontsize
        configuration.ApplicationConfig().set_key_value('USER', 'fontsize', str(size))

    def get_style(self, s_type):
        file = open(style_path + '/' + s_type, "r")
        style = file.read()
        file.close()
        return style


class ToggleSwitch(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCheckable(True)
        self.setMinimumWidth(66)
        self.setMinimumHeight(22)

    def paintEvent(self, event):
        label = "ON" if self.isChecked() else "OFF"
        bg_color = Qt.green if self.isChecked() else Qt.red

        radius = 10
        width = 32
        center = self.rect().center()

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.translate(center)
        painter.setBrush(QtGui.QColor(0, 0, 0))

        pen = QtGui.QPen(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawRoundedRect(QRect(-width, -radius, 2 * width, 2 * radius), radius, radius)
        painter.setBrush(QtGui.QBrush(bg_color))
        sw_rect = QRect(-radius, -radius, width + radius, 2 * radius)
        if not self.isChecked():
            sw_rect.moveLeft(-width)
        painter.drawRoundedRect(sw_rect, radius, radius)
        painter.drawText(sw_rect, Qt.AlignCenter, label)
