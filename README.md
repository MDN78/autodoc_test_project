# Проект по тестированию сервиса поиска и подбора автозпчастей "Автодок"    

----
> [Сайт Автодок.ру](https://www.autodoc.ru/)   
> 
![](https://github.com/MDN78/qa_guru_python_10_15/blob/master/assets/autodoc_main_page.PNG)  
----
## Список проверок, реализованных в автотестах:  

### UI автотесты:  
- [x] Проверка формы авторизации на сайте
- [x] Авторизация пользователя на сайте (в процессе доработки)  
- [x] Авторизация незарегестрированнного пользователя
- [x] Проверка загрузки главной страницы сайта
- [x] Поиск автозапчасти по номеру
- [x] Поиск каталога по VIN номеру автомобиля

----
### Проект реализован с использованием:  
<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="selene" src="https://github.com/MDN78/MDN78/blob/main/assets/selene.png"></code>
<code><img width="5%" title="selenium" src="https://github.com/MDN78/MDN78/blob/main/assets/selenium.png"></code>
<code><img width="5%" title="pytest" src="https://github.com/MDN78/MDN78/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="selenoid" src="https://github.com/MDN78/MDN78/blob/main/assets/selenoid.png"></code>
<code><img width="5%" title="jenkins" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="allure" src="https://github.com/MDN78/MDN78/blob/main/assets/allure_testops.png"></code>
<code><img width="5%" title="github" src="https://github.com/MDN78/MDN78/blob/main/assets/github.png"></code>  

----
### Локальный запуск  

Для локального запуска необходимо выполнить команду в терминале:  
```commandline
pytest
```

----

### Удаленный запуск автотестов выполняется на сервере Jenkins  
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_MDN782007_qa_guru_python_10_15/">Ссылка на проект в Jenkins</a>

----
## Параметры сборки:

`ENVIRONMENT` - определение среды сборки, по умолчанию `PROD`  
`BROWSER NAME` - выбор браузера  
`BROWSER VERSION` - выбор версии браузера. По умолчанию выбран браузер Chrome, версия 100  
`COMMENT` - комментарий для получателя уведомления в Телеграмм  


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_MDN782007_qa_guru_python_10_15/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать браузер
4. Выбрать версию браузера
4. Указать комментарий для уведомления в Телеграмм
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure
