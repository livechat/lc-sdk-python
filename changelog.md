# Change Log
All notable changes to this project will be documented in this file.

## [0.2.2] - TBA

### Changed
- Added new param `owner_client_id` in Configuration API `create_bot` for Interface and v3.5 classes.

## [0.2.1] - 2022-02-16

### Changed
- Handling of configuration file.

## [0.2.0] - 2022-01-31

### Added
- API stable version 3.4 as a default.
- API dev preview version 3.5 support.
- Proxy support to web interfaces.
- RtmResponse structure for RTM clients.

## [0.1.10] - 2021-12-02

### Added

- Added new methods related to greetings conversion, chat surveys, and response time in reports-api v3.4.

## [0.1.9] - 2021-11-03

### Added

- Added new methods for organization/license ID lookup in configuration v3.4.

### Changed

- Fixed methods for uploading files.
- Renamed `reorder_auto_access` to `update_auto_access`

## [0.1.8] - 2021-10-21

### Added

- Added logging for web interface

## [0.1.7] - 2021-10-13

### Changed

- Support for `organization_id` in Customer(rtm/web) v3.4.

## [0.1.6] - 2021-10-06

### Added

- Added type hints support
- Added support for reports-api.

### Changed

- Refactored ws_client module - new client extends WebSocketApp from websocket-client package.
- Handling for `pushes` param in `login` of agent RTM.

## [0.1.5] - 2021-09-07

### Changed

- websocket-client package to version 1.2.1.
- urllib package to version 1.26.6.


## [0.1.4] - 2021-08-26

### Added

- Support for HTTP/2 protocol within the following clients: Agent(web), Customer(web), Configuration.

### Changed

- requests to httpx package.


## [0.1.3] - 2021-08-05

### Added

- Handle new destructive action flags (`ignore_requester_presence`, `ignore_agents_availability`) in v3.4.

### Bugfixes

- Include essential subpackages


## [0.1.2] - 2021-07-29

### Added

- Api version 3.4 support.
- Example usages of following clients: Agent(rtm/web), Customer(rtm/web), Configuration.
- `add_user_to_chat` and `send_typing_indicator` methods to v3.4 class with a support of visibility arg.
- Custom header handling for the following clients: Agent(web), Customer(web), Configuration.

### Removed

- Support for `grant_chat_access` and `revoke_chat_access` methods in v3.4 class.
- Flag `require_active_thread` in method `add_user_to_chat`.

### Changed

- urllib package to version 1.26.5.


## [0.1.1] - 2021-04-06

### Added

- New header manipulation/retrieval methods.
- Changelog file.
- Simple usage example in `readme.md`.

### Changed

- `agent`, `configuration` and `customer` packages now have common root `livechat`.
- rename `ConfigurationApi` method for obtaining client to `get_client` for consistency with other clients.
