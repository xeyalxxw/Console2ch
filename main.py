import requests

# https://2ch.hk/makaba/mobile.fcgi?task=get_boards  ===== Список досок


def get_boards():
	boards = requests.get('https://2ch.hk/makaba/mobile.fcgi?task=get_boards').json()

	for key in boards:
		print(key + ':\n')
		for board in boards[key]:
			print('  /' + board['id'] + '/ ' + board['name'])
		print('\n\n')

def get_threads(board, page):
	if page == '0':
		page = 'index'
	threads = requests.get('https://2ch.hk/' + board + '/' + page + '.json').json()
	print('' + threads['Board'] + ' /' + threads['BoardName'])
	if page == 'index':
		page = '0'
	print(page + ' страница\n\n')
	for thread in threads['threads']:
		print('\n' + ('='*50))
		print(thread['posts'][0]['name'] + '   |   ' + '#' + thread['posts'][0]['num'] + '   |   ' + thread['posts'][0]['date'])
		if thread['posts'][0]['subject'] == '':
			pass
		else:
			print(thread['posts'][0]['subject'])
		print(thread['posts'][0]['comment'])
		print('Ответов: ' + str(thread['posts'][0]['posts_count']))


while True:
	user = input()
	if user == 'b':
		get_threads(user, '0')





