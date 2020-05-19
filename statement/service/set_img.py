from PIL import Image, ImageFont, ImageDraw
from datetime import datetime


def certificate(username_fille, first_name, last_name,  full_name, course, SP, reg_number):

    img = Image.open('static/certificate/Сертификат.jpg')
    idrew = ImageDraw.Draw(img)
    font_username = ImageFont.truetype('static/fonts/SourceSerifPro-Semibold.ttf', size=210)
    font_course = ImageFont.truetype('static/fonts/SourceSerifPro-Semibold.ttf', size=115)
    font_text = ImageFont.truetype('static/fonts/SourceSerifPro-Semibold.ttf', size=130)

    username = f"{last_name} {first_name}"

    date = datetime.now().strftime("%Y-%m-%d")

    idrew.text((450, 1030), username, font=font_username, fill='#4E67AA')

    idrew.text((450, 1300), full_name, font=font_username, fill='#4E67AA')

    idrew.text((1150, 1535), course, font=font_course, fill='#4E67AA')

    if SP == 'Программное обеспечение вычислительной техники и автоматизированных систем':
        course_title_1 = 'Программное обеспечение вычислительной'
        course_title_2 = 'техники и автоматизированных систем'
        idrew.text((450, 1690), course_title_1, font=font_text, fill='#4E67AA')
        idrew.text((450, 1880), course_title_2, font=font_text, fill='#4E67AA')

    elif SP == 'Автоматизированные системы обработки информации и управления':
        course_title_1 = 'Автоматизированные системы обработки '
        course_title_2 = 'информации и управления'
        idrew.text((450, 1690), course_title_1, font=font_text, fill='#4E67AA')
        idrew.text((450, 1880), course_title_2, font=font_text, fill='#4E67AA')

    elif SP == 'Техническое обслуживание средств вычислительной техники и компьютерных сетей':
        course_title_1 = 'Техническое обслуживание средств'
        course_title_2 = 'вычислительной техники и компьютерных сетей'
        idrew.text((450, 1690), course_title_1, font=font_text, fill='#4E67AA')
        idrew.text((450, 1880), course_title_2, font=font_text, fill='#4E67AA')

    else:
        idrew.text((450, 1690), SP, font=font_text, fill='#4E67AA')

    idrew.text((1850, 2065), reg_number, font=font_text, fill='#4E67AA')

    idrew.text((510, 2665), date, font=font_text, fill='#4E67AA')

    img.convert('RGB')
    img.save(f'static/certificate/user-certificate/{username_fille}.png')

    return f'static/certificate/user-certificate/{username_fille}.png'
