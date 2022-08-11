import json, datetime, urllib.request
from os.path import exists

class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at
        # should return true otherwise
        if exists('ratios.json'):
            today = str(datetime.date.today())
            with open('ratios.json', 'r') as json_file:
                
                data = json.load(json_file)

            for i in data["converter"]:
                if i['base_currency'] == self.base and i['target_currency'] == self.target and i['date_fetched'] == today:
                    return True
            return False
        else:
            with open('ratios.json', 'a') as file:
                start_of_json_file = {
                    "converter": []
                }
                json.dump(start_of_json_file, file)


    def fetch_ratio(self):
        url = 'https://api.exchangerate.host/convert'
        params = {
            'from': self.base,
            "to": self.target,
        }
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string
        with urllib.request.urlopen(url) as response:
            data = response.read()
            encoding = response.info().get_content_charset('utf-8')
            data = json.loads(data.decode(encoding))
            ratio = data['result']
            self.save_ratio(ratio)


    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        creating_object = True
        with open('ratios.json', 'r+') as outfile:
            file = json.load(outfile)
            for i in file["converter"]:
                if i['base_currency'] == self.base and i['target_currency'] == self.target:
                    i["date_fetched"] = today
                    i["ratio"] = ratio
                    creating_object = False
                
                json.dumps(i, indent=4)
            outfile.seek(0)
            outfile.truncate()

            if creating_object:
                 today = str(datetime.date.today())
                 data = {
                    "base_currency": self.base,
                    "target_currency": self.target,
                    "date_fetched": today,
                    "ratio": ratio
                    }
                 file["converter"].append(data)
            json.dump(file, outfile, indent=4)
            

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        with open('ratios.json') as json_file:
            data = json.load(json_file)
            for i in data["converter"]:
                if i['base_currency'] == self.base and i['target_currency'] == self.target:
                    return i['ratio']
        
