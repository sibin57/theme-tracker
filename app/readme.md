Чтобы запустить сервер, необходимо импортировать всю необходимую информацию:  

  $ pyinstaller --onefile --add-data templates:templates --add-data static:static --add-data db-themes.db:.--hidden-import app.py  
  
Затем можно запускать сам сервер 

  $ flask run  
  
Приложение выведет информацию о том, на каком адресе оно работает  
По умолчанию это **127.0.0.1:5000**
