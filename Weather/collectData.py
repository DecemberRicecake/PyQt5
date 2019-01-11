# -*- coding: UTF-8 -*-


def get_front_data(self):
    front_data = {}
    # env_check = self.radioButton_qa.isChecked()   # 处理单选框
    # front_data["env"] = str(sel_env(env_check))
    # front_data["phoneNum"] = str(self.account.text())  # 处理文本框
    # front_data["city"] = str(sel_identity(identity_index))
    # front_data["Amount"] = str(self.amountSpinBox.value())    # 处理数字输入框
    front_data["city"] = str(self.cityComboBox.currentText())
    return front_data

# def sel_env(env_check):
#     if env_check:
#         env = "qa"
#     else:
#         env = "main"
#     return env
