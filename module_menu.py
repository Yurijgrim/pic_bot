
import telebot,wget
from telebot import types 


def keys_admin():
    return(
    "Пользователи",
    "Парсер",
    'Статистика',
    'Меню')
 

def keys_admin_users():
    return (
    "Список",
    "Тарифы",
    'Меню')


def keys_admin_parser():
    return (
    "Информация",
    "Сегмент Фото",
    "Сегмент Видео",
    "Сегмент Аниме"
    'Меню')


def keys_start():
	return(
	"Профиль",
	"Видео",
	"Фото",
	"Космос")

def keys_me():
	return(
	"Тариф",
	"Избранное",
	"Обновление",
	'Меню')


def keys_pay():
	return(
	"Тариф 1час"
	"Тариф 1день",
	"Тариф 7дней",
	"Тариф 30дней",
	"Тариф VIP безлимит",
	'Меню')


def keys_saved():
	return(
	"<<<<",
	">>>>",
	"Смотреть",
	"Убрать",
	'Меню')


def keys_anime():
	return(
	"<",
	">",
	"В избранное",
	'Меню')



def keys_photo():
	return(
	"<<",
	">>",
	"В избранное",
	'Меню')



def keys_video():
	return(
	"<<<",
	">>>",
	"Смотреть",
	"В избранное",
	'Меню')