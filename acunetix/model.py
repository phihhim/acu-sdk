from .api_call import APICall

class Target:
    def __init__(self, id, address, description="", criticality=10, continuous_mode=False,
    manual_intervention=None, type=None,verification=None, status=None, scans=[]):
        self.id = id
        self.address = address
        self.description = description
        self.criticality = criticality
        self.continuous_mode = continuous_mode
        self.manual_intervention = manual_intervention
        self.type = type
        self.verification = verification
        self.scans = scans
        self.status = status

    def __repr__(self):
        rep = self.id
        return str(rep)


class Scan:
    def __init__(self, id, profile, incremental=False,
    max_scan_time=0, next_run=None, report=None, schedule=None, target=None, results=None):
        self.id = id
        self.profile = profile
        self.incremental = incremental
        self.max_scan_time = max_scan_time
        self.next_run = next_run
        self.report = report
        self.schedule = schedule
        self.target = target
        if results is None:
            results = []

    def __repr__(self):
        rep = self.id
        return str(rep)

class Result:
    def __init__(self, id, start_date, scan, end_date=None, status=""):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.scan = scan

    def __repr__(self):
        rep = self.id
        return str(rep)

class VulnDesciption:
    def __init__(self, id, name, cvss2, cvss3, cvss_score, description, details,
    highlights, impact, long_description, recommendation, references, request, response_info, source, tags):
        self.id = id
        self.name = name
        self.cvss2 = cvss2
        self.cvss3 = cvss3
        self.cvss_score = cvss_score
        self.description = description
        self.details = details
        self.highlights = highlights
        self.impact = impact
        self.long_description = long_description
        self.recommendation = recommendation
        self.references = references
        self.request = request
        self.response_info = response_info
        self.source = source
        self.tags = tags

    def __repr__(self):
        rep = self.id
        return str(rep)

class Vulnerability:
    def __init__(self, id, name, affects_url, affects_detail, confidence, criticality, last_seen, severity, status, result):
        self.id = id
        self.name = name
        self.affects_url = affects_url
        self.affects_detail = affects_detail
        self.confidence = confidence
        self.criticality = criticality
        self.last_seen = last_seen
        self.severity = severity
        self.status = status
        self.result = result

    def __repr__(self):
        rep = self.id
        return str(rep)

    def detail(self, api, token):
        endpoint = '/scans/{}/results/{}/vulnerabilities/{}'.format(
            self.result.scan.id, self.result.id, self.id)
        new_call = APICall(api, token)
        response = new_call.get(endpoint)
        id = response['vt_id']
        name = response['vt_name']
        cvss2 = response['cvss2']
        cvss3 = response['cvss3']
        cvss_score = response['cvss_score']
        description = response['description']
        details = response['details']
        highlights = response['highlights']
        impact = response['impact']
        long_description = response['long_description']
        recommendation = response['recommendation']
        references = response['references']
        request = response['request']
        response_info = response['response_info']
        source = response['source']
        tags = response['tags']

        return VulnDesciption(id, name, cvss2, cvss3, cvss_score, description, details, highlights,
                              impact, long_description, recommendation, references, request, response_info, source, tags)


class Location:
    def __init__(self, loc_id, loc_type, name, parent, path, source, tags, result):
        self.loc_id = loc_id
        self.loc_type = loc_type
        self.name = name
        self.parent = parent
        self.path = path
        self.source = source
        self.tags = tags
        self.result = result

    def childrens(self, api, token):
        try:
            new_call = APICall(api, token)
            response = new_call.get('/scans/{}/results/{}/crawldata/{}/children'.format(self.result.scan.id, self.result
                                                                                        .id, self.loc_id))
            raw_locations = response['locations']

            locations = []

            for location in raw_locations:
                loc_id = location['loc_id']
                loc_type = location['loc_type']
                name = location['name']
                parent = None
                path = location['path']
                source = None
                tags = location['tags']

                locations.append(Location(loc_id, loc_type, name, parent, path, source, tags, self.result))

            return locations
        except:
            return []