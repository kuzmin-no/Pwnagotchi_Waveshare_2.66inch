# Pwnagotchi v1.5.5 patch for screen Waveshare 2.66'

Screen 2.66inch E-Paper E-Ink Display Module (B), 296×152, Red / Black / White, SPI
https://www.waveshare.com/product/2.66inch-e-paper-module-b.htm

To install patch execute following commands on Raspberry Pi.
It will require access to Internet and root access
```
git clone https://github.com/kuzmin-no/Pwnagotchi_Waveshare_2.66inch.git
./Pwnagotchi_Waveshare_2.66inch/Pwnagotchi_Waveshare_2.66inch.sh
```

Update config file ```config.toml``` as showed below
```
ui.display.enabled = true
ui.display.type = "waveshare266inch"
ui.display.color = "black"
```
and restart ```pwnagotchi``` service
```
sudo systemctl start pwnagotchi
```
