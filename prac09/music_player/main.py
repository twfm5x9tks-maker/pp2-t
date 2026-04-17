import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Music Player")
done = False
clock = pygame.time.Clock()
pygame.mixer.init()
volume = 0.5
pygame.mixer.music.set_volume(volume)

tracks = [{"music":"music/Monetochka_-_Tvojo_imya_56229294.mp3", "image":"image/tvoeimya.png"}, 
          {"music":"music/Dajjte_tank_-_CHekhov_69873612.mp3", "image":"image/chehov.png"}, 
          {"music":"music/Dajjte_tank_-_Lyudi_68398361.mp3", "image":"image/ludi.png"}, 
          {"music":"music/Monetochka_-_Padat_v_gryaz_64293978.mp3", "image":"image/padatvg.png"}, 
          {"music":"music/Dajjte_tank_-_My_60573704.mp3", "image":"image/my.png"}, 
          {"music":"music/Dajjte_tank_-_Malenkijj_64714984.mp3", "image":"image/malenkuy.png"}, 
          {"music":"music/Monetochka_-_Monopoliya_77840938.mp3", "image":"image/monopol.png"}]
current_track = 0

current_image = pygame.image.load(tracks[current_track]["image"])
current_image = pygame.transform.scale(current_image, (400,400))

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

pygame.mixer.music.load(tracks[current_track]["music"])
pygame.mixer.music.play()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_s:
                pygame.mixer.music.pause()
            if event.key == pygame.K_n:
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track]["music"])

                current_image = pygame.image.load(tracks[current_track]["image"])
                current_image = pygame.transform.scale(current_image, (400,400))
                pygame.mixer.music.play()
            if event.key == pygame.K_b:
                current_track = (current_track-1)%len(tracks)
                pygame.mixer.music.load(tracks[current_track]["music"])

                current_image = pygame.image.load(tracks[current_track]["image"])
                current_image = pygame.transform.scale(current_image, (400,400))
                pygame.mixer.music.play()

            if event.key == pygame.K_UP:
                volume = min(1.0, volume +0.1)
                pygame.mixer.music.set_volume(volume)

            if event.key == pygame.K_DOWN:
                volume = max(0.0, volume-0.1)
                pygame.mixer.music.set_volume(volume)
            

            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        
        if event.type == MUSIC_END:
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track]["music"])
                current_image = pygame.image.load(tracks[current_track]["image"])
                current_image = pygame.transform.scale(current_image, (400,400))
                pygame.mixer.music.play()

    screen.fill((255,255,255))
    rect = current_image.get_rect(center = (800//2, 600//2))
    screen.blit(current_image, rect)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()