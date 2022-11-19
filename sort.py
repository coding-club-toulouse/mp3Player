#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame
import mutagen.mp3
import mutagen.oggvorbis
from mutagen.easyid3 import EasyID3
from datetime import timedelta
 
def get_info(f, item):
    """ En parallele a get_tag() """
    try:
        return f[item][0]
    except:
        return ""
 
def get_tag(path):
    """ Obtention des tags mp3 ou ogg """
    ext = path[-3:]
 
    # Tag du MP3
    if ext == 'mp3':
        zik = mutagen.mp3.MP3(path)
        try:
            f = EasyID3(path)
        except:
            f = zik
    # Tag du OGG
    elif ext == 'ogg':
        zik = mutagen.oggvorbis.OggVorbis(path)
        f = zik
    else:
        raise Exception(f"Invalid file passed: {path}")
 
    # Info sur le fichier musical
    length = str(int(zik.info.length))
    bitrate = str(int(zik.info.bitrate / 1024))
    sample_rate = str(zik.info.sample_rate / 1000.)
 
    # Obtention des tags
    rep={}
    rep['artist'] = get_info(f, 'artist')  or "unknown"
    rep['album'] = get_info(f, 'album') or "unknown"
    rep['title'] = get_info(f, 'title') or "unknown"
    rep['bitrate'] = bitrate
    rep['sample_rate'] = sample_rate
    rep['duree'] = length
    rep['genre'] = get_info(f, 'genre') or "unknown"
    rep['composer'] = get_info(f, 'composer') or "unknown"
    rep['date'] = get_info(f, 'date') or "unknown"
    rep['tracknumber'] = get_info(f, 'tracknumber') or "unknown"
 
    return rep

def find_music(direct, option):
    for element in os.listdir(direct):
        if element.endswith(('.mp3', '.ogg')):
            path = direct+element
            target = get_tag(path)
            if option == 'long' and int(target['duree']) >= 240:
                print(target)
                pygame.mixer.init()
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()
            elif option == 'short' and int(target['duree']) < 240:
                print(target)
                pygame.mixer.init()
                pygame.mixer.music.load(path)
                pygame.mixer.music.play()

def is_playing():
    return pygame.mixer.music.get_busy()

def get_music_position():
    if is_playing():
        position = timedelta(milliseconds=pygame.mixer.music.get_pos())
        return position.total_seconds()
    else:
        return 0
