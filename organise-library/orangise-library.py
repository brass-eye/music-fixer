#! /usr/bin/python3
import os
import string
import sys

'''
This is shit. Write it again using os.walk
'''

# for root, dirs, files in os.walk('/home/aiden/Music'):
    # print(root)
    # print(dirs)
    # print(files)
    # print()
def capitalise(word):
    if not word.isupper():
        word = string.capwords(word) \
            .replace('Dj','DJ') \
            .replace('Fp-oner','FP-Oner') \
            .replace('Deepchord', 'DeepChord')
    return word


manual = []
working_dir = os.path.abspath(sys.argv[1])
# can u use a comprehension to filter out the not directories here
for directory in os.listdir(working_dir):
    if '.mp3' not in directory and 'mosse' not in directory:
        directory_parts = directory.split(' - ')
        if len(directory_parts) > 1:
            artist = capitalise(directory_parts[0])
            album = capitalise(' - '.join(directory_parts[1:]))
            new_directory = working_dir + '/sorted1/' + artist + '/' + album 
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            full_path = (working_dir + '/' + directory)
            print("mv " + full_path + " " + new_directory)
            os.rename( full_path, new_directory )
            # for f in os.listdir(full_path):
                # print("w: " + directory + "/" + f + " to: " +  new_directory + "/" + f)

    else:
        manual.append(directory)

# for manual_dir in manual:


#print(manual)



# directories = directories here

# dirs_with_dashed = directories with at least one dash surrounded by space " - " 
# manual = differnce of dirs_with_dashed and directories

# foreach dirs_with_dashed do

    # split on " - "
    # 0 = artist
    # 1 = album
    # if artist doens't exsit
        # mkdir artist

    # get album yeat
    # mkdir "(YEAR) - $album"
    # copy dir/* to artist/album

# done


# foreach manual as man
    # if not manual exists
        #mkdir manual
    # mv man manual/man

# done

#Test cases
    #rrose and Rrose doesn't make two directories
    #fp-oner
    #dirs with more than one ' - '
    # capitalise
        # Dj sprinkles -> DJ Sprinkles
        # Dj Sprinkles -> DJ Sprinkles
