import os
import mutagen
 
path_str = '/run/media/aiden/ff338d33-962c-47d0-87b9-64849ab5c715/Music2/Music'
home_music = '~/Music'

rootDir = os.path.expanduser(home_music)
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):

    directory_artists = {}
    for fname in fileList:
        if fname.endswith(('mp3', 'flac')):
            path = os.path.join(dirName, fname)
            try:
                track = mutagen.File(path, easy=True)
                artist = track['artist'][0]
                directory_artists[artist] = True
                # add if unique to artists array for this dir
                    #lower case it and warn if theres some case mismatch 
                    
            except AttributeError as identifier:
                #print("\t\tfound non music file: " + path )
                pass
            except KeyError as error:
                #print("\t\tfound non music file: " + path )
    #            print ('error on path {}'.format(path))
                pass
            except TypeError as error:
                #print("\t\tfound non music file: " + path )
                # print ('header erorr on path {}'.format(path))
                pass

            # if the unique artists > 1 then set all the tracks to have TPE = ?
    if len(directory_artists) > 1:
        print("{} is probably a comp".format(dirName))