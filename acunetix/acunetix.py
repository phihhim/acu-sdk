from .api_call import APICall
from .model import Target, Scan, Result, Vulnerability, Location
import re
import json
from pprint import pprint
class Acunetix:
    def __init__(self, api: str, token: str):
        self.api = api
        self.token = token

    def __str__(self):
        return f'Acunetix: {self.api} token {self.token}'

    def __repr__(self):
        return f'Acunetix: {self.api} token {self.token}'

    def create_target(self, url, description=""):
        if not re.fullmatch(
                r"^(http://www\.|https://www\.|http://|https://)?[a-z0-9]+([\-.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(/.*)?$",
                url, re.IGNORECASE):
            return None

        data = {
            "targets": [
                {
                    "address": url,
                    "description": description
                }
            ],
            "groups": []
        }
        new_call = APICall(self.api, self.token)
        respose = new_call.post('/targets/add', data)
        target = respose['targets'][0]
        id = target['target_id']
        address = target['address']
        criticality = target['criticality']
        description = target['description']
        type = target['type']

        return Target(id, address, description, criticality, type=type)


    def create_targets(self, list_target):
        r = re.compile(
            r"^(http://www\.|https://www\.|http://|https://)?[a-z0-9]+([\-.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(/.*)?$",
            re.IGNORECASE)
        tmp_targets = []

        for i in list_target:
            url = str(i['address'])
            if r.match(url):
                tmp_targets.append(i)

        data = {
            "targets": tmp_targets,
            "groups": []
        }
        try:
            new_call = APICall(self.api, self.token)
            respose = new_call.post('/targets/add', data)
            raw_targets = respose['targets']

            targets = []

            for target in raw_targets:
                id = target['target_id']
                address = target['address']
                criticality = target['criticality']
                description = target['description']
                type = target['type']

                targets.append(
                    Target(id, address, description, criticality, type=type))

            return targets

        except:
            return []

    def get_all_targets(self):
        try:
            new_call = APICall(self.api, self.token)
            response = new_call.get('/targets')
            raw_targets = response['targets']
            targets = []

            for target in raw_targets:
                id = target['target_id']
                address = target['address']
                description = target['description']
                criticality = target['criticality']
                continuous_mode = target['continuous_mode']
                manual_intervention = target['manual_intervention']
                type = target['type']
                verification = target['verification']
                status = target['last_scan_session_status']

                new_target = Target(id, address, description, criticality, continuous_mode,
                                    manual_intervention, type, verification, status)

                targets.append(new_target)

            return targets

        except:
            return None

    def get_target_by_id(self, id):
        try:
            id = id.strip()
            id = id.lower()
            if len(id) > 255:
                return None
            new_call = APICall(self.api, self.token)
            target = new_call.get('/targets/{}'.format(id))
            id = target['target_id']
            address = target['address']
            description = target['description']
            criticality = target['criticality']
            continuous_mode = target['continuous_mode']
            manual_intervention = target['manual_intervention']
            type = target['type']
            verification = target['verification']

            new_target = Target(id, address, description, criticality,
                                continuous_mode, manual_intervention, type, verification)
            return new_target

        except:
            return None


    def get_targets_by_ids(self, list_id):
        all_target = self.get_all_targets()
        for i in range(len(list_id)):
            list_id[i] = list_id[i].strip()
            list_id[i] = list_id[i].lower()
        targets = [x for x in all_target if x.id in list_id]
        return targets

    def delete_targets(self, ids):
        ids = [x for x in ids if len(x) <= 255]
        data = {
            "target_id_list": ids
        }
        new_call = APICall(self.api, self.token)
        return new_call.post_raw('/targets/delete', data)
    # scan

    def create_scan(self, target, profile_id,
                                schedule=None):
        if schedule is None:
            schedule = {"disable": False, "start_date": None, "time_sensitive": False}
        if len(profile_id) > 255:
            return None
        data = {
            "profile_id": profile_id,
            "incremental": False,
            "schedule": schedule,
            "target_id": target.id
        }
        try:
            new_call = APICall(self.api, self.token)
            res = new_call.post_raw('/scans', data)
            #response = json.loads(res.text)
            scan_id = res.headers['Location'].split('/')[-1]
            '''
            scan_id = res.headers['Location'].split('/')[-1]
            incremental = response['incremental']
            max_scan_time = response['max_scan_time']

            new_scan = Scan(id=scan_id, profile=profile_id, incremental=incremental,
                            max_scan_time=max_scan_time, schedule=schedule, target=target)
            '''
            return scan_id
        except:
            return None

    def get_all_scans(self):
        try:
            new_call = APICall(self.api, self.token)
            response = new_call.get('/scans')
            raw_scans = response['scans']
            return raw_scans

        except:
            return []

    def get_scan_by_id(self, scan_id):
        try:
            scan_id = scan_id.strip()
            scan_id = scan_id.lower()
            if len(scan_id) > 255:
                return None
            new_call = APICall(self.api, self.token)
            scan = new_call.get('/scans/{}'.format(scan_id))
            id = scan['scan_id']
            profile = scan['profile_id']
            incremental = scan['incremental']
            max_scan_time = scan['max_scan_time']
            next_run = scan['next_run']
            report = scan['report_template_id']
            schedule = scan['schedule']

            new_scan = Scan(id, profile, incremental=incremental,
                            max_scan_time=max_scan_time, next_run=next_run, report=report, schedule=schedule)

            return new_scan
        except:
            return None

    def get_scans_by_ids(self, list_id):
        all_scans = self.get_all_scans()
        for i in range(len(list_id)):
            list_id[i] = list_id[i].strip()
            list_id[i] = list_id[i].lower()
        scans = [x for x in all_scans if x.id in list_id]
        return scans

    def pause_scan(self, scan):
        new_call = APICall(self.api, self.token)
        return new_call.post_raw('/scans/{}/pause'.format(scan.id))

    def resume_scan(self, scan):
        new_call = APICall(self.api, self.token)
        return new_call.post_raw('/scans/{}/resume'.format(scan.id))

    def stop_scan(self, scan):
        new_call = APICall(self.api, self.token)
        return new_call.post_raw('/scans/{}/abort'.format(scan.id))

    def delete_scan(self, scan):
        id = scan.id
        if len(id) > 255:
            return None
        new_call = APICall(self.api, self.token)
        return new_call.delete_raw('/scans/{}'.format(id))

    # result
    def get_results_of_scan(self, scan_id):
        new_call = APICall(self.api, self.token)
        response = new_call.get('/scans/{}/results'.format(scan_id))

        return response['results'][0]['result_id']


    # vulnerability
    def get_vulns_of_result(self, result_id, scan_id):
        try:
            new_call = APICall(self.api, self.token)
            response = new_call.get('/scans/{}/results/{}/vulnerabilities'.format(result_id, scan_id))
            raw_vulns = response['vulnerabilities']

            

            return response

        except:
            return []

    def get_result_statistic(self, scan_id, result_id):
        new_call = APICall(self.api, self.token)
        return new_call.get('/scans/{}/results/{}/statistics'.format(scan_id, result_id))

    # location
    def get_root_location(self, result):
        try:
            new_call = APICall(self.api, self.token)
            response = new_call.get('/scans/{}/results/{}/crawldata/0/children'.format(result.scan.id, result.id))
            raw_location = response['locations'][0]
            loc_id = raw_location['loc_id']
            loc_type = raw_location['loc_type']
            name = raw_location['name']
            parent = None
            path = raw_location['path']
            source = None
            tags = raw_location['tags']

            return Location(loc_id, loc_type, name, parent, path, source, tags, result)

        except:
            return None
