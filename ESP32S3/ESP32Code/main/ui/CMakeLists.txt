SET(SOURCES screens/ui_Screen1.c
    screens/ui_Screen2.c
    ui.c
    components/ui_comp_hook.c
    ui_helpers.c
    images/ui_img_youtube_png.c
    images/ui_img_amazon_png.c
    images/ui_img_duolingo_png.c
    images/ui_img_spotify_png.c
    images/ui_img_discord_png.c
    images/ui_img_instagram_png.c
    images/ui_img_netflix_png.c
    images/ui_img_photoshop_png.c
    images/ui_img_whatsapp_png.c
    images/ui_img_vs_code_png.c
    images/ui_img_github_png.c
    images/ui_img_calculator_png.c
    images/ui_img_text_extractor_png.c
    images/ui_img_notion_png.c
    images/ui_img_1531840258.c
    images/ui_img_cut_png.c
    images/ui_img_copy_png.c
    images/ui_img_paste_png.c
    images/ui_img_hibernate_png.c
    images/ui_img_shutdown_png.c
    images/ui_img_home_png.c
    images/ui_img_mic_png.c
    images/ui_img_mute_png.c
    images/ui_img_back_png.c)

add_library(ui ${SOURCES})
