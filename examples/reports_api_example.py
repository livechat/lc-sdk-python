''' Reports API client example usage. '''

from livechat.reports.base import ReportsApi

# Get number of chats occured during specified period.
reports_api = ReportsApi.get_client(token='<your access token>')
chats_occured = reports_api.total_chats(filters={
    'to': '2020-09-14T23:59:59+02:00',
    'from': '2020-09-01T00:00:00+02:00'
})
print(chats_occured.json())

# Get distribution of tags for chats.
tags_distribution = reports_api.tags(filters={
    'to': '2020-09-14T23:59:59+02:00',
    'from': '2020-09-01T00:00:00+02:00'
},
                                     distribution='day')
print(tags_distribution.json())
