# Changelog — Standby Clock by YAHBALLON

## [0.1.2] — 2026-11-02

- First standalone source and release in **Yahballon/PS5_StandbyClock**, originally developed in **Yahballon/tmp_lap**.
- Replace the generated clock tile with the approved AI-generated red-neon logo **without the outer red ring**.
- Add the supplied user interface design screenshot to **screenshots/** and display it in a redesigned README.
- Rebuild the native PS5 eboot and installer ZIP with the new 512×512 **sce_sys/icon0.png**; retain Title ID **PPSA99876** and saved preferences.
- Preserve v0.1.1 live weather, approximate IP geolocation, OLED pixel shift/auto dim, and AM/PM positioning fix.

## [0.1.1] — 2026-11-02

- Live weather in the former HOMEBREW/READY tile; requests via TLS, cached fallback.
- Fixed 12-hour AM/PM suffix appearing under the giant clock.
- OLED guard: full-screen shift, idle/night dim and periodic black rest.
- PS5 native release in tmp_lap.

## [0.1.0] — 2026-11-02

- Initial clock dashboard, analog seconds, calendar, foreground alarm and saved settings.

**Hardware note:** Native CI success is a compile/package result, not a claim of verified operation on every jailbroken console.
