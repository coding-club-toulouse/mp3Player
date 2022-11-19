#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame
from pygame import mixer
from pygame import time
import mutagen.mp3
import mutagen.oggvorbis
from mutagen.easyid3 import EasyID3
 
def get_info(f, item):
    """ En parallele a get_tag() """
    try:
        return f[item][0]
    except:
        return ""
 
def get_tag(path):
    """ Obtention des tags mp3 ou ogg """
    ext = path[-3:]
    flag = 'on'
 
    # Tag du MP3
    if ext == 'mp3':
        zik = mutagen.mp3.MP3(path)
        try:
            f = EasyID3(path)
        except:
            flag = 'off'   
    # Tag du OGG
    if ext == 'ogg':
        zik = mutagen.oggvorbis.OggVorbis(path)
        f = zik
 
    # Info sur le fichier musical
    length = str(int(zik.info.length))
    bitrate = str(int(zik.info.bitrate / 1024))
    sample_rate = str(zik.info.sample_rate / 1000.)
 
    # Obtention des tags
    if flag != 'off':
        album = get_info(f, 'album')
        title = get_info(f, 'title')
        artist = get_info(f, 'artist')
        genre = get_info(f, 'genre')
        composer = get_info(f, 'composer')
        date = get_info(f, 'date')
        tracknumber = get_info(f, 'tracknumber')
    else:
        album = 'unknown'
        title = 'unknown'
        artist = 'unknown'
        genre = 'unknown'
        composer = 'unknown'
        date = 'unknown'
        tracknumber = 'unknown'
 
    rep={}
    rep['artist']=artist
    rep['album']=album
    rep['title']=title
    rep['bitrate']=bitrate
    rep['sample_rate']=sample_rate
    rep['duree']=length
    rep['genre']=genre
    rep['composer']=composer
    rep['date']=date
    rep['tracknumber']=tracknumber
 
    return rep

def find_music(direct, option):
    for element in os.listdir(direct):
        if element.endswith('.mp3'):
            path = direct+element
            target = get_tag(path)
            if option == 'long':
                if int(target['duree']) >= 240:
                    print(target)
                    pygame.mixer.init()
                    clock = pygame.time.Clock()
                    pygame.mixer.music.load(path)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        print("Playing....")
                        clock.tick(1000)
            elif option == 'short':
                if int(target['duree']) < 240:
                    print(target)
                    pygame.mixer.init()
                    clock = pygame.time.Clock()
                    pygame.mixer.music.load(path)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        continue
