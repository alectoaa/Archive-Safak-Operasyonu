import sys
import random
import pygame

pygame.init()
pygame.mixer.init()

GENISLIK = 1600
YUKSEKLIK = 925
ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
pygame.display.set_caption("Şafak Operasyonu")

try:
    icon = pygame.image.load("kılıç.png")
    pygame.display.set_icon(icon)
except pygame.error:
    pass

SIYAH = (0, 0, 0)
BEYAZ = (255, 255, 255)
MAVI = (0, 0, 255)
KIRMIZI = (255, 0, 0)
GRI = (105, 105, 105)
YESIL = (0, 128, 0)
BORDO = (128, 0, 0)
GUMUS = (192, 192, 192)

clock = pygame.time.Clock()
FPS = 60


class GirisEkrani:
    def __init__(self):
        self.font_baslik = pygame.font.Font(None, 80)
        self.font_metin = pygame.font.Font(None, 36)
        
        self.baslik = self.font_baslik.render("Şafak Operasyonu", True, BORDO)
        self.metin = self.font_metin.render("Başlamak için bir zorluk seviyesi seçin:", True, BORDO)
        
        self.baslik_rect = self.baslik.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 - 120))
        self.metin_rect = self.metin.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 - 50))
        
        self.kolay_buton = pygame.Rect(GENISLIK // 2 - 100, YUKSEKLIK // 2 + 10, 200, 45)
        self.orta_buton = pygame.Rect(GENISLIK // 2 - 100, YUKSEKLIK // 2 + 70, 200, 45)
        self.zor_buton = pygame.Rect(GENISLIK // 2 - 100, YUKSEKLIK // 2 + 130, 200, 45)
        self.kurallar_buton = pygame.Rect(GENISLIK // 2 - 100, YUKSEKLIK // 2 + 190, 200, 45)
        self.cikis_buton = pygame.Rect(GENISLIK // 2 - 100, YUKSEKLIK // 2 + 250, 200, 45)

        self.kolay_metin = self.font_metin.render("Kolay", True, SIYAH)
        self.orta_metin = self.font_metin.render("Orta", True, SIYAH)
        self.zor_metin = self.font_metin.render("Zor", True, SIYAH)
        self.kurallar_metin = self.font_metin.render("Kurallar", True, SIYAH)
        self.cikis_metin = self.font_metin.render("Çıkış", True, SIYAH)

    def goster(self):
        while True:
            clock.tick(FPS)
            for olay in pygame.event.get():
                if olay.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if olay.type == pygame.MOUSEBUTTONDOWN and olay.button == 1:
                    pos = olay.pos
                    if self.kolay_buton.collidepoint(pos):
                        return 100, "Kolay"
                    elif self.orta_buton.collidepoint(pos):
                        return 300, "Orta"
                    elif self.zor_buton.collidepoint(pos):
                        return 500, "Zor"
                    elif self.kurallar_buton.collidepoint(pos):
                        self.goster_kurallar()
                    elif self.cikis_buton.collidepoint(pos):
                        pygame.quit()
                        sys.exit()

            ekran.fill(SIYAH)
            ekran.blit(self.baslik, self.baslik_rect)
            ekran.blit(self.metin, self.metin_rect)

            pygame.draw.rect(ekran, YESIL, self.kolay_buton, border_radius=8)
            pygame.draw.rect(ekran, MAVI, self.orta_buton, border_radius=8)
            pygame.draw.rect(ekran, KIRMIZI, self.zor_buton, border_radius=8)
            pygame.draw.rect(ekran, GRI, self.kurallar_buton, border_radius=8)
            pygame.draw.rect(ekran, GUMUS, self.cikis_buton, border_radius=8)

            ekran.blit(self.kolay_metin, self.kolay_metin.get_rect(center=self.kolay_buton.center))
            ekran.blit(self.orta_metin, self.orta_metin.get_rect(center=self.orta_buton.center))
            ekran.blit(self.zor_metin, self.zor_metin.get_rect(center=self.zor_buton.center))
            ekran.blit(self.kurallar_metin, self.kurallar_metin.get_rect(center=self.kurallar_buton.center))
            ekran.blit(self.cikis_metin, self.cikis_metin.get_rect(center=self.cikis_buton.center))

            pygame.display.flip()

    def goster_kurallar(self):
        k_baslik_font = pygame.font.Font(None, 60)
        k_font = pygame.font.Font(None, 28)
        
        baslik = k_baslik_font.render("Kurallar", True, BEYAZ)
        baslik_rect = baslik.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 - 180))
        
        satirlar = [
            "1. Oyuncuyu yön tuşları (W, A, S, D) ile kontrol edebilirsiniz.",
            "2. Boşluk tuşuna basarak zorbaya ateş edebilirsiniz.",
            "3. Zorba size yaklaşırsa oyun biter, bu yüzden mesafenizi koruyun.",
            "4. Oyunu kazanmak için hedef skora ulaşmanız gerekmektedir.",
            "5. ESC tuşuna basarak oyunu duraklatabilirsiniz.",
            "6. İyi eğlenceler!"
        ]
        
        rendered_satirlar = []
        for i, satir in enumerate(satirlar):
            txt = k_font.render(satir, True, BEYAZ)
            rect = txt.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 - 100 + (i * 40)))
            rendered_satirlar.append((txt, rect))

        while True:
            clock.tick(FPS)
            for olay in pygame.event.get():
                if olay.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if olay.type == pygame.KEYDOWN:
                    if olay.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        return

            ekran.fill(SIYAH)
            ekran.blit(baslik, baslik_rect)
            for txt, rect in rendered_satirlar:
                ekran.blit(txt, rect)
                
            pygame.display.flip()


class Oyuncu(pygame.sprite.Sprite):
    def __init__(self, mermi_grubu):
        super().__init__()
        self.image = pygame.image.load("ATEŞ EDEN ÇOCUK.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = GENISLIK // 2
        self.rect.bottom = YUKSEKLIK - 50
        self.hiz = 5
        self.mermi_grubu = mermi_grubu
        
        try:
            self.mermi_sesi = pygame.mixer.Sound("9mm-pistol-shoot-short-reverb-7152.mp3")
        except pygame.error:
            self.mermi_sesi = None

    def update(self):
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_a]:
            self.rect.x -= self.hiz
        if tuslar[pygame.K_d]:
            self.rect.x += self.hiz
        if tuslar[pygame.K_w]:
            self.rect.y -= self.hiz
        if tuslar[pygame.K_s]:
            self.rect.y += self.hiz

        self.rect.clamp_ip(ekran.get_rect())

    def atesle(self):
        if len(self.mermi_grubu) < 3:
            if self.mermi_sesi:
                self.mermi_sesi.play()
            Mermi(self.rect.centerx, self.rect.top, self.mermi_grubu)


class Mermi(pygame.sprite.Sprite):
    def __init__(self, x, y, grup):
        super().__init__()
        ham_resim = pygame.image.load("MERMİ.png").convert_alpha()
        self.image = pygame.transform.rotate(ham_resim, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.hiz = 10
        grup.add(self)

    def update(self):
        self.rect.y -= self.hiz
        if self.rect.bottom < 0:
            self.kill()


class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def die(self):
        self.rect.x = random.randint(50, GENISLIK - 100)
        self.rect.y = random.randint(50, YUKSEKLIK // 2)


class AnaMenuDugme:
    def __init__(self):
        self.rect = pygame.Rect(GENISLIK // 2 - 100, YUKSEKLIK // 2 + 100, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.metin = self.font.render("Ana Menüye Dön", True, SIYAH)
        self.metin_rect = self.metin.get_rect(center=self.rect.center)

    def draw(self, ekran):
        pygame.draw.rect(ekran, MAVI, self.rect, border_radius=6)
        ekran.blit(self.metin, self.metin_rect)


class BitisEkrani:
    def __init__(self, skor, zorluk, kazandi=False):
        self.font_baslik = pygame.font.Font(None, 80)
        self.font_skor = pygame.font.Font(None, 36)
        
        durum_metni = "Tebrikler, Kazandınız!" if kazandi else "Oyun Bitti"
        self.baslik = self.font_baslik.render(durum_metni, True, BORDO)
        self.skor_metin = self.font_skor.render(f"Skor: {skor}", True, BEYAZ)
        self.zorluk_metin = self.font_skor.render(f"Zorluk: {zorluk}", True, BEYAZ)
        
        self.baslik_rect = self.baslik.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 - 80))
        self.skor_metin_rect = self.skor_metin.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 - 10))
        self.zorluk_metin_rect = self.zorluk_metin.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 + 30))
        
        self.ana_menu_dugme = AnaMenuDugme()

    def goster(self):
        while True:
            clock.tick(FPS)
            for olay in pygame.event.get():
                if olay.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if olay.type == pygame.MOUSEBUTTONDOWN and olay.button == 1:
                    if self.ana_menu_dugme.rect.collidepoint(olay.pos):
                        return

            ekran.fill(SIYAH)
            ekran.blit(self.baslik, self.baslik_rect)
            ekran.blit(self.skor_metin, self.skor_metin_rect)
            ekran.blit(self.zorluk_metin, self.zorluk_metin_rect)
            
            self.ana_menu_dugme.draw(ekran)

            pygame.display.flip()


class DurduEkrani:
    def __init__(self):
        self.font = pygame.font.Font(None, 80)
        self.font_alt = pygame.font.Font(None, 36)
        self.baslik = self.font.render("Oyun Duraklatıldı", True, BORDO)
        self.devam_metin = self.font_alt.render("Devam etmek için ESC'ye basın", True, BEYAZ)
        self.baslik_rect = self.baslik.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 - 30))
        self.devam_rect = self.devam_metin.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 + 40))

    def goster(self):
        while True:
            clock.tick(FPS)
            for olay in pygame.event.get():
                if olay.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if olay.type == pygame.KEYDOWN and olay.key == pygame.K_ESCAPE:
                    return

            ekran.fill(SIYAH)
            ekran.blit(self.baslik, self.baslik_rect)
            ekran.blit(self.devam_metin, self.devam_rect)
            pygame.display.flip()


def oyunu_baslat():
    giris = GirisEkrani()
    hedef_skor, zorluk = giris.goster()

    mermi_grup = pygame.sprite.Group()
    oyuncu_grup = pygame.sprite.Group()
    npc_grup = pygame.sprite.Group()

    oyuncu = Oyuncu(mermi_grup)
    oyuncu_grup.add(oyuncu)

    npc = NPC(100, 100, "NPC.png")
    npc_grup.add(npc)

    skor = 0
    font = pygame.font.Font(None, 40)
    calisiyor = True

    while calisiyor:
        clock.tick(FPS)

        for olay in pygame.event.get():
            if olay.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif olay.type == pygame.KEYDOWN:
                if olay.key == pygame.K_SPACE:
                    oyuncu.atesle()
                elif olay.key == pygame.K_ESCAPE:
                    DurduEkrani().goster()

        oyuncu_grup.update()
        mermi_grup.update()

        carpisimlar = pygame.sprite.groupcollide(mermi_grup, npc_grup, True, False)
        if carpisimlar:
            skor += 10
            npc.die()

        ekran.fill(SIYAH)
        oyuncu_grup.draw(ekran)
        mermi_grup.draw(ekran)
        npc_grup.draw(ekran)

        skor_txt = font.render(f"Skor: {skor} / {hedef_skor}", True, BEYAZ)
        ekran.blit(skor_txt, (30, 30))

        if skor >= hedef_skor:
            bitis = BitisEkrani(skor, zorluk, kazandi=True)
            bitis.goster()
            calisiyor = False

        if pygame.sprite.spritecollideany(oyuncu, npc_grup):
            bitis = BitisEkrani(skor, zorluk, kazandi=False)
            bitis.goster()
            calisiyor = False

        pygame.display.flip()


if __name__ == "__main__":
    while True:
        oyunu_baslat()