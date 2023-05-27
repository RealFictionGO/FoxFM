from moviepy.editor import concatenate_audioclips, AudioFileClip
from os import getcwd, listdir

def join_all_audio(audio_files_names:list, output_name:str) -> None:
    audio_files = []
    for sound in audio_files_names:
        audio_files.append(AudioFileClip(sound))

    full_audio = concatenate_audioclips(audio_files)

    """ TODO: Preventing from overwriting output audio file
    ld = listdir()
    fformat = output_name.split('.')[-1]
    output_name = output_name.replace("."+fformat, '')
    
    
    if output_name + "." + fformat in ld:
        print(True)
        new_output_name = output_name
        couter = 1
        while new_output_name in ld:
            new_output_name = output_name
            new_output_name = f"{new_output_name}({couter}).{fformat}"
            print(new_output_name)
            couter += 1

        output_name = new_output_name
        print("\n---- NEW NAME -----\n")
    """
    full_audio.write_audiofile(output_name)
