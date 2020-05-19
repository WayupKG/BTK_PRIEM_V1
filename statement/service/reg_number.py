from .set_img import certificate


# регистрационный номер Сертификат
def reg_numbr_certificate(user_statement, sp, course, forma='Контракт',  corres='Очный'):
    if sp == 'ТМ' and forma == 'Бюджет':
        if user_statement.reg_number < 10:
            reg_num = f'20ТМ10{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТМ1{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ТЭС' and forma == 'Бюджет':
        if user_statement.reg_number < 10:
            reg_num = f'20ТЭС10{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТЭС1{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭСТ' and forma == 'Бюджет':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭСТ0{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭСТ1{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ТЭС' and forma == 'Бюджет':
        if user_statement.reg_number < 10:
            reg_num = f'20ТЭС10{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТЭС1{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭС' and forma == 'Бюджет':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭС10{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭС1{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'АСОИ' and forma == 'Бюджет':
        if user_statement.reg_number < 10:
            reg_num = f'20АСОИ30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20АСОИ3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    # 9 Класс Контракт ------------------------------------------------------------
    elif sp == 'ТМ' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20ТМ20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТМ2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'СП' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20СП20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20СП2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ПО' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20ПО20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ПО2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ТО' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20ТО20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТО2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'АСОИ' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20АСОИ20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20АСОИ2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ТЭС' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20ТЭС20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТЭС2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭСТ' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭСТ20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭСТ2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭС' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭС20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭС2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ГР' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20ГР20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ГР2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'БУ' and forma == 'Контракт' and course == '1':
        if user_statement.reg_number < 10:
            reg_num = f'20БУ20{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20БУ2{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    # 11 Класс Контракт ------------------------------------------------------------
    elif sp == 'ТМ' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20ТМ30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТМ3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'СП' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20СП30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20СП3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ПО' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20ПО30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ПО3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ТО' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20ТО30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТО3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'АСОИ' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20АСОИ30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20АСОИ3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ТЭС' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20ТЭС30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТЭС3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭСТ' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭСТ30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭСТ3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭС' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭС30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭС3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ГР' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20ГР30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ГР3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'БУ' and forma == 'Контракт' and course == '2' and corres == 'Очный':
        if user_statement.reg_number < 10:
            reg_num = f'20БУ30{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20БУ3{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    # 11 Класс Контракт Заочный ------------------------------------------------------------
    elif sp == 'ТМ' and forma == 'Контракт' and course == '2' and corres == 'Заочный':
        if user_statement.reg_number < 10:
            reg_num = f'20ТМ40{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТМ4{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ПО' and forma == 'Контракт' and course == '2' and corres == 'Заочный':
        if user_statement.reg_number < 10:
            reg_num = f'20ПО40{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ПО4{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ТЭС' and forma == 'Контракт' and course == '2' and corres == 'Заочный':
        if user_statement.reg_number < 10:
            reg_num = f'20ТЭС40{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ТЭС4{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭСТ' and forma == 'Контракт' and course == '2' and corres == 'Заочный':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭСТ40{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭСТ4{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    elif sp == 'ЭС' and forma == 'Контракт' and course == '2' and corres == 'Заочный':
        if user_statement.reg_number < 10:
            reg_num = f'20ЭС40{user_statement.reg_number}'
            user_statement.registor_index = reg_num

        else:
            reg_num = f'20ЭС4{user_statement.reg_number}'
            user_statement.registor_index = reg_num

    user_statement.save()

    if course == '1':
        if user_statement.patronymic is not None:
            user_statement.image_certificate_priom = certificate(user_statement.user, user_statement.first_name,
                                                                 user_statement.last_name, user_statement.patronymic,
                                                                 '1', user_statement.specialty, user_statement.registor_index)
        else:
            user_statement.image_certificate_priom = certificate(user_statement.user, user_statement.first_name,
                                                                 user_statement.last_name, '',
                                                                 '1', user_statement.specialty,
                                                                 user_statement.registor_index)
    elif course == '2':
        if user_statement.patronymic is not None:
            user_statement.image_certificate_priom = certificate(user_statement.user, user_statement.first_name,
                                                                 user_statement.last_name, user_statement.patronymic,
                                                                 '2', user_statement.specialty,
                                                                 user_statement.registor_index)
        else:
            user_statement.image_certificate_priom = certificate(user_statement.user, user_statement.first_name,
                                                                 user_statement.last_name, '',
                                                                 '2', user_statement.specialty,
                                                                 user_statement.registor_index)
    user_statement.save()
