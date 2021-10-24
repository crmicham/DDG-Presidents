import requests

presidents_list = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe',
                   'Adams', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk',
                   'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
                   'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland',
                   'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft',
                   'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt',
                   'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon',
                   'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush',
                   'Obama', 'Trump', 'Biden']

url_ddg = "https://api.duckduckgo.com/presidents%20of%20the%20united%20states?ia=web"


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data['RelatedTopics']
    print(str(rsp_data['RelatedTopics']))
    for sub in related_topics:
        for name in presidents_list:
            if name in str(sub['Text']):
                break
        else:
            assert False
    else:
        assert True


test_ddg0()

