# Change Log
All notable changes to this project will be documented in this file.

## [0.1.3] - 2021-07-29

### Added

- `add_user_to_chat` and `send_typing_indicator` methods to v3.4 class with a support of visibility arg.
- Custom header handling for the following clients: Agent(rtm/web), Customer(rtm/web), Configuration.

### Removed

- Support for `grant_chat_access` and `revoke_chat_access` methods in v3.4 class.
- Flag `require_active_thread` in method `add_user_to_chat`.

### Updated

- urllib package to version 1.26.5.


## [0.1.2] - 2021-04-13

### Added

- Api version 3.4 support.
- Example usages of following clients: Agent(rtm/web), Customer(rtm/web), Configuration.


## [0.1.1] - 2021-04-06

### Added

- New header manipulation/retrieval methods.
- Changelog file.
- Simple usage example in `readme.md`.

### Changed

- `agent`, `configuration` and `customer` packages now have common root `livechat`.
- rename `ConfigurationApi` method for obtaining client to `get_client` for consistency with other clients.
