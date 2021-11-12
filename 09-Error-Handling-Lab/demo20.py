# d = {'baba': 1}
#
# for k, v in d.items():
#     d['dqdo'] = 2 # will result in RuntimeError: dictionary changed size during iteration

try:
    d = {'baba': 1}
    assert d['baba'] == 2 # AssertionError
    for k, v in d.items():
        d['dqdo'] = 2
except (RuntimeError, ValueError, TypeError):
    print('error happened')
except AssertionError:
    print('I tried to assert something that was falase')

# moje da dobavqme neogranichen broi except klauzi kum edin try blok