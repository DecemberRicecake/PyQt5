# -*- coding: utf-8 -*-
import HttpAction
import config


def login(data):
    allurl = config.MS1_API[data["env"]] + "api/Account/Login"
    datap = {
        "Account": data["phoneNumber"],
        "Pwd": "afdd0b4ad2ec172c586e2150770fbf9e",
        "Code": "string",
        "CitySubstationID": 3,
        "IP": "string",
        "LoginType": 1,
        "LoginSource": 0
    }
    result = HttpAction.newpost(allurl, datap, "")
    data["token"] = result["Content"]["Token"]
    # print(rzr_data)
    return data
