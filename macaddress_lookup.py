import requests
import re
import sys
from tabulate import tabulate


class MacLookup:
    def __init__(self, macaddress):
        self.macaddress = macaddress

    def is_valid_mac(self):
        pattern = re.compile("(([0-9A-Fa-f]{2}[.:]?){5}[0-9A-Fa-f]{2})")
        if pattern.match(self.macaddress): return True
        return False

    def macaddress_lookup_request(self):
        url = "https://api.macaddress.io/v1"
        payload = {
            "output":"json",
            "search":self.macaddress
        }
        headers = {
            "X-Authentication-Token": None  # ADD YOUR APIKEY HERE ("APIKEY")
        }

        if headers["X-Authentication-Token"]:
            r = requests.get(url, headers=headers, params=payload)
            response = r.json()
            return response
        return ""

    def tab_mac_info(self):
        mac_response = self.macaddress_lookup_request()
        headers = [["Vendor Details"], ["Block Details"], ["MAC Address Details"]]
        vendor = mac_response["vendorDetails"]
        table_vendor = [
            ["OUI", vendor["oui"]],
            ["Is Private", vendor["isPrivate"]],
            ["Company Name", vendor["companyName"]],
            ["Company Address", vendor["companyAddress"]],
            ["Country Code", vendor["countryCode"]]
        ]
        block = mac_response["blockDetails"]
        table_block = [
            ["Block Found", block["blockFound"]],
            ["Border Left", block["borderLeft"]],
            ["Border Right", block["borderRight"]],
            ["Block Size", block["blockSize"]],
            ["Assignment Block Size", block["assignmentBlockSize"]],
            ["Date Created", block["dateCreated"]],
            ["Date Updated", block["dateUpdated"]]
        ]
        mac = mac_response["macAddressDetails"]
        table_mac = [
            ["Search Term", mac["searchTerm"]],
            ["Is Valid", mac["isValid"]],
            ["Virtual Machine", mac["virtualMachine"]],
            ["Applications", mac["applications"]],
            ["Transmission Type", mac["transmissionType"]],
            ["Administration Type", mac["administrationType"]],
            ["Wireshark Notes", mac["wiresharkNotes"]],
            ["Comment", mac["comment"]],
        ]
        return tabulate(table_vendor, tablefmt="psql"), tabulate(table_block, tablefmt="psql"), tabulate(table_mac, tablefmt="psql")


def main():
    try:
        mac_add = sys.argv[1]
        mac = MacLookup(mac_add)
        if mac.is_valid_mac():
            mac.macaddress_lookup_request()
            res_vendor, res_block, res_mac = mac.tab_mac_info()
            print("Vendor Details")
            print(res_vendor + "\n")
            print("Block Details")
            print(res_block + "\n")
            print("MAC address details")
            print(res_mac + "\n")
        else:
            print("INSERT VALID MAC")
    except IndexError:
        print("PLEASE INSERT A MAC ADDRESS")
    except TypeError:
        print("MISSING TOKEN, PLEASE SIGN UP FOR https://macaddress.io TO GET YOUR TOKEN")


main()
