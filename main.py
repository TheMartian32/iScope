

def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue
        return inp


def main():

    # * User inputs
    print('\n*---------------------------------------*')
    circumference = ask_for(
        'What is the circumference of the base?: ', 'Not an answer', float)
    ref_azimuth = ask_for(
        '\nWhat is the azimuth that you want as a reference point?: ', 'Not an answer', float)

    marker = ask_for(
        '\nWhere is the white marker on the tape measure?: ', 'Not an answer', float)

    tar_azimuth = ask_for(
        '\nWhat is the target azimuth?: ', 'Not an answer', float)
    print('*---------------------------------------*')

    # * Grabbing degrees, delta actual, and final degrees
    current_deg = 360*marker / circumference
    delta_actual = tar_azimuth - ref_azimuth
    final_deg = current_deg+delta_actual

    # * Where the marker should be on the tape measure
    to_rope_point = (final_deg/360)*circumference

    if to_rope_point > circumference:
        to_rope_point -= circumference

    if to_rope_point < 0:
        to_rope_point += circumference

    return print(f'\nPut marker here: {to_rope_point}')


if __name__ == "__main__":
    main()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        print(
            '\nTyping Y will restart the script, typing N will terminate it.')
        repeat = input(
            '\nDo you need any more information? (Y/N): ').lower()
        if repeat[0] == 'y':
            main()
            continue
        if repeat[0] == 'n':
            break
