### Вставная терминология  
#1.0. возвращает структуру {var} из хранилища, или, если там
Null - создает ее, помещает в хранилище и возвращает ее (структуру).  
#1.1. возвращает переменную {var} из хранилища, или, если она равна
Null - читает ее из файла, сохраняет в хранилище и возвращает переменную.  

### Arxitecture  
```text
bot/  
|—📁funs/  
    |—📁lists/  *//saved through SQL*
        |—📄users.py  
            |—⚪️get_users_list()  
            |—⚪️add_in_users_list()  
            |—⚪️del_from_users_list()  
            |—... *//different actions*  
        |—... *//different lists*  
    |—📁get_entity/  
        |—📄config_t.py  
            |—get_token() *//#1.1{значения токена}*  
        |—📄core_t.py  
            |—get_bot() *//#1.0{бота}*  
            |—get_router() *//#1.0{роутера}*  
    |—... *//next topics*  
    |—📁src/  
        |—📁lists/  *//saved through SQL*
            |—📄users.py  
                |—⚪️get_users_list_src()  
                |—⚪️add_in_users_list_src()  
                |—⚪️del_from_users_list_src()
                |—... *//dufferent actions*  
            |—... *//different lists*  
        |—📁get_entity/  
            |—📄config_t.py  
                |—get_token_src()  
            |—📄core_t.py  
                |—get_bot_src() *//#1.0{бота}*  
                |—get_router_src() *//#1.0{роутера}*  
    |—... *//next topics*  
|—📁headers/  
    |—📄welcome.py //group_1  
        |—⚪️cm_start_header()  
        |—🔴cm_help_header()  *//Not implemented*  
    |—📄group_2.py  
        |—⚪️...  
        |—⚪️...  
    |—... *//different cm groups*  
|—📁src/  
    |—📄welcome.py //group_1  
        |—⚪️cm_start_src()  
        |—🔴cm_help_src()  *//Not implemented*  
    |—📄group_2.py  
        |—⚪️...  
        |—⚪️...  
    |—... *//different cm groups*  
|—📁frontend/  
    |—📁welcome/ //group_1  
        |—📄texts.py  
        |—📄cm_start.gif  
        |—📄reply.py  
        |—📄buttons.py  
        |—📁src/  
            |—📄reply.py  
            |—📄buttons.py  
    |—📁group_2/  
        |—📄texts.py  
        |—📄reply.py  
        |—📄buttons.py  
        |—📁src/  
            |—📄reply.py  
            |—📄buttons.py  
    |—...  
|—📁data/  
    |—📄config.json  
        |—⚪️token  
        |—⚪️...  
    |—📁lists/  
        |—📄admins.db  
        |—📄users.db  
        |—...  
    |—📁logs/  
        |—📄owner.log  
        |—📄совладелец.log  
    |—...  
    // создание разделов для сохранения предпочтений об админах.  
|—📁storage/ *// used with 'import ...'*  
    |—📄config.py  
        |—⚪️token=Null *//string*  
        |—⚪️... *//other*  
    |—📄core.py  
        *//save core structs*  
        |—⚪️router=Router()  
        |—⚪️bot=Bot("TOKEN")  
        |—⚪️... *//others*  
```