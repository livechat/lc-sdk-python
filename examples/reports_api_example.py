''' Reports API client example usage. '''

from livechat.reports.client import ReportsApi

# Get number of chats occured during specified period.
reports_api = ReportsApi.get_client(token='<your access token>')
chats_occured = reports_api.total_chats(date_to='2020-09-14T23:59:59+02:00',
                                        date_from='2020-09-01T00:00:00+02:00')
print(chats_occured.json())

# Get distribution of tags for chats v3.3.
payload = {
    'to': '2020-09-14T23:59:59+02:00',
    'from': '2020-09-01T00:00:00+02:00',
    'distribution': 'day'
}
tags_distribution = reports_api.tags(payload=payload)
print(tags_distribution.json())

# Get distribution of tags for chats v3.4.
reports_api = ReportsApi.get_client(token='<your access token>', version='3.4')
tags_distribution = reports_api.tags()
print(tags_distribution.json())
