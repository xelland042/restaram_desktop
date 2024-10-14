run.mob:
	flet run main.py
run.mob.test:
	flet run test.py
run.mob.w:
	flet run main.py -w -r
run.mob.a:
	flet run main.py --android -r
compile:
	pybabel compile -d locales -D messages --use-fuzzy
update:
	pybabel update -d locales -D messages -i locales/messages.pot