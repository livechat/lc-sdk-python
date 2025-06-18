# Change Log
All notable changes to this project will be documented in this file.

## [0.4.2] - TBA

### Added
- New method `delete_event` in customer-api v3.6.
- New methods in configuration-api v3.6 for greetings: `create_greeting`, `delete_greeting`, `get_greeting`, `update_greeting`, `list_greetings`.

### Changed
- Improved websocket response collection + extended logging in the websocket client.

### Bugfixes
- Fixed version in websocket url for customer-api v3.4 and v3.6.

## [0.4.1] - 2025-04-23

### Added
- New `groups`, `queued_visitors`, `queued_visitors_left`, `unique_visitors` methods in reports-api v3.6.

### Changed
- Corrected the `surveys` report to `forms` in reports-api v3.5 & v3.6.

## [0.4.0] - 2025-02-14

### Added
- New `get_company_details`, `list_customer_bans` and `unban_customer` methods in configuration-api v3.6.
- Added `response_timeout` parameter in `open_connection` methods.
- New `get_license_info` method in agent-api v3.5.
- New `update_session` method in agent-api v3.6 (rtm).
- Allow passing custom header for websocket handshake.

### Changed
- Added missing top-level arguments to `update_auto_access` method in configuration-api.
- Updated outdated packages.
- Changed pre-commit flake8 URL

## [0.3.9] - 2024-04-22

### Added
- New methods in configuration-api v3.5, v3.6 for bot management: `create_bot_template`, `delete_bot_template`, `update_bot_template`, `list_bot_templates`, `issue_bot_token`, `reset_bot_secret`, `reset_bot_template_secret`.

### Changed
- Updated outdated packages.
- Enhanced error logging for improved troubleshooting: Automatically includes response headers in the log for server errors, providing detailed information (such as x-debug-id) for more effective issue diagnosis.
- Enhanced timeouts for the RTM and WEB clients.
- Introduced `AccessToken` structure which allows keeping token type in separate field. Previous way of passing tokens as a string of format `type: token` remains supported for backwards compatibility.

### Bugfixes
- Enabled instantiation for `CustomerRtmV36` within the 3.6 version of the Customer RTM API.
- Adjusted the return types in `get_client` method across RTM and WEB clients.
- Fixed an issue where messages in the WebSocket client were incorrectly shared across all instances.
- Fixed `upload_file` method in agent-api v3.4/v3.5/v3.6 classes.

## [0.3.8] - 2023-11-30

### Added
- Support for `logout` method in agent-api v3.6 web class.
- Support for `agent_id` parameter in agent-api v3.6 `logout` method.

### Changed
- Implemented truncation of request params in logging for large data.

### Bugfixes
- Allow sending rtm events as a bot by adding `author_id` param.

## [0.3.7] - 2023-09-26

### Added

- `reactivate_email` and `update_company_details` actions in configuration-api v3.6 class.
- `disable_logging` flag for web based clients.

### Changed
- [Loguru](https://pypi.org/project/loguru/) used for logging.
- Required packages to currently newest versions.

### Bugfixes
- Fix HTTP request type for `get_product_source` method in Configuration API v3.5 and v3.6.
- Fix an issue related to fetching responses in RTM.

## [0.3.6] - 2023-03-09

### Added

- Added support for billing-api.
- New `highest_available` option for `customer_monitoring_level` in agent-api `login` method.

### Bugfixes
- Fix `customer_monitoring_level` parameter in `login` method in agent-api v3.3/v3.4/v3.5 classes.
- Fix `httpx` version in setup.cfg

### Removed

- Support for `list_customers` method in agent-api v3.6 classes.

## [0.3.5] - 2022-11-25

### Added
- Support for new batch methods in configuration-api v3.5: `batch_create_bots`, `batch_delete_bots`, `batch_update_bots`.
- Support for new version 3.6.

### Changed
- Config now points to v3.5 as stable and 3.6 as dev-preview version.

## [0.3.4] - 2022-10-26

### Added
- New methods in configuration-api v3.5: `list_groups_properties`, `get_product_source`.
- Support for `default_group_priority` parameter in `create_bot` and `update_bot` methods in configuration-api v3.3/v3.4/v3.5 classes.
- Support for `job_title` parameter in `create_bot` method in configuration-api v3.3/v3.4/v3.5 classes.
- Support for `proxies` and `verify` parameters for web base clients.

### Changed
- Renamed method `tag_chat_usage` to `chat_usage` in reports-api v3.5.
- Internal documentation main page and structure.

### Bugfixes
- Fix paths for `response_time` and `first_response_time` methods in reports-api v3.4/v3.5 classes.
- Fix `upload_file` method in agent-api v3.4/v3.5 classes.

### Removed
- Support for `list_group_properties`, `get_license_id` and `get_organization_id` method in configuration-api v3.5 class.
- Support for `webhook` parameter in `create_bot` and `update_bot` methods in configuration-api v3.3/v3.4/v3.5 classes.

## [0.3.3] - 2022-07-20

### Added
- Support for new batch methods in configuration-api v3.5: `batch_create_agents`, `batch_delete_agents`, `batch_update_agents`, `batch_approve_agents`, `batch_suspend_agents`, `batch_unsuspend_agents`.

### Changed
- Updated requirements.txt.

### Bugfixes
- Fix HTTP method in `get_dynamic_configuration`, `get_configuration`, `get_localization`, `list_group_properties`, `list_license_properties` and `delete_event_properties`.
- Fix `upload_file` method by changing the way of uploading files; using HTTP multipart encoding.

## [0.3.2] - 2022-06-20

### Added
- Webhooks support. Allows to easily convert webhook's body into parsed data classes.

## [0.3.1] - 2022-05-26

### Changed
- Updated httpx dependency to a version which fixes a potential vulnerability.
- Updated readme file and extended examples with getting pushes from the websocket client.

## [0.3.0] - 2022-05-10

### Added
- New methods in configuration-api v3.5 for tags management: `create_tag`, `list_tags`, `update_tag`, `delete_tag`.
- New method in reports-api v3.5 for getting tags usage statistics in chats: `tags_chat_usage`.

### Changed
- Major refactoring: classes with API methods for each version are now held in separate modules
  This is possibly breaking change, please make sure if your imports point to `livechat.<service>.<transport>.base`).
  When in doubt, please compare with the updated `examples` directory.
- Added new param `owner_client_id` in Configuration API `create_bot` for Interface and v3.5 classes.
- Added new methods related to product information (`list_channels`, `check_product_limits`) in Configuration API v3.5.

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
