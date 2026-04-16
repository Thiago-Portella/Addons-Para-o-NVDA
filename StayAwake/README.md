# StayAwake (NVDA Add-on)

StayAwake is a lightweight NVDA add-on that prevents Windows from automatically locking or sleeping while it is enabled.

It uses a safe, supported Windows API and does not simulate mouse or keyboard input.

## Features

- Toggle system idle prevention on or off
- Announce current StayAwake status
- Does not interfere with normal NVDA or system behavior
- Automatically releases the system state when NVDA exits

## Default Keyboard Shortcuts

- **NVDA + Ctrl + Shift + I**  
  Toggle StayAwake on or off

- **NVDA + Ctrl + Shift + A**  
  Announce whether StayAwake is currently enabled

All shortcuts can be changed in:
NVDA Menu → Preferences → Input Gestures → StayAwake

## Notes

- StayAwake only prevents automatic idle sleep or lock.
- It does not disable Windows power settings permanently.
- It does not generate fake mouse or keyboard activity.

## License

MIT License
