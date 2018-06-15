import os
import mutagen
 
path_str = '/run/media/aiden/ff338d33-962c-47d0-87b9-64849ab5c715/Music2/Music'
home_music = '~/Music'
# Set the directory you want to start from
rootDir = os.path.expanduser(path_str)
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    # print('Found directory: %s' % dirName)
    for fname in fileList:
        path = os.path.join(dirName, fname)
        directory_artists = {}
        try:
            track = mutagen.File(path, easy=True)
            # artist = 
            # directory_artists[track.]
            # add if unique to artists array for this dir
                #lower case it and warn if theres some case mismatch 
                
            if type(track) is mutagen.flac.FLAC: 
                print(track['date'])
        except AttributeError as identifier:
            #print("\t\tfound non music file: " + path )
            pass
        except KeyError as error:
            #print("\t\tfound non music file: " + path )
#            print ('error on path {}'.format(path))
            pass
        except mutagen.mp3.HeaderNotFoundError as error:
            #print("\t\tfound non music file: " + path )
            # print ('header erorr on path {}'.format(path))
            pass

        # if the unique artists > 1 then set all the tracks to have TPE = ?