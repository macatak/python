#!/usr/bin/python3

'''
Faker 101 script
'''

from faker import Faker

faker = Faker()

# this will print outthe function calls
#print(dir(faker))
'''
# more useful ones
print(f'name: {faker.name()}')
print(f'address: {faker.address()}')
#print(f'text: {faker.text()}')
print(f'ascii_company_email: {faker.ascii_company_email()}')
print(f'chrome: {faker.chrome()}')
print(f'date_time_this_month: {faker.date_time_this_month()}')
'''

print(f'address: {faker.address()}')
print(f'am_pm: {faker.am_pm()}')
print(f'android_platform_token: {faker.android_platform_token()}')
print(f'ascii_company_email: {faker.ascii_company_email()}')
print(f'ascii_email: {faker.ascii_email()}')
print(f'ascii_free_email: {faker.ascii_free_email()}')
print(f'ascii_safe_email: {faker.ascii_safe_email()}')
#print(f'bank_country: {faker.bank_county()}')
print(f'bban: {faker.bban()}')
#print(f'binary: {faker.binary'()}')
print(f'boolean: {faker.boolean()}')
print(f'bothify: {faker.bothify()}')
print(f'bs: {faker.bs()}')
print(f'building_number: {faker.building_number()}')
print(f'catch_phrase: {faker.catch_phrase()}')
print(f'century: {faker.century()}')
print(f'chrome: {faker.chrome()}')
print(f'city: {faker.city()}')
print(f'city_prefix: {faker.city_prefix()}')
print(f'city_suffix: {faker.city_suffix()}')
print(f'color_name: {faker.color_name()}')
print(f'company: {faker.company()}')
print(f'company_email: {faker.company_email()}')
print(f'company_suffix: {faker.company_suffix()}')
print(f'coordinate: {faker.coordinate()}')
print(f'country: {faker.country()}')
print(f'country_code: {faker.country_code()}')
print(f'credit_card_expire: {faker.credit_card_expire()}')
print(f'credit_card_full: {faker.credit_card_full()}')
print(f'credit_card_number: {faker.credit_card_number()}')
print(f'credit_card_provider: {faker.credit_card_provider()}')
print(f'credit_card_security_code: {faker.credit_card_security_code()}')
print(f'cryptocurrency: {faker.cryptocurrency()}')
print(f'cryptocurrency_code: {faker.cryptocurrency_code()}')
print(f'cryptocurrency_name: {faker.cryptocurrency_name()}')
print(f'currency: {faker.currency()}')
print(f'currency_code: {faker.currency_code()}')
print(f'currency_name: {faker.currency_name()}')
print(f'date: {faker.date()}')
print(f'date_between: {faker.date_between()}')
print(f'date_between_dates: {faker.date_between_dates()}')
print(f'date_object: {faker.date_object()}')
print(f'date_of_birth: {faker.date_of_birth()}')
print(f'date_this_century: {faker.date_this_century()}')
print(f'date_this_decade: {faker.date_this_decade()}')
print(f'date_this_month: {faker.date_this_month()}')
print(f'date_this_year: {faker.date_this_year()}')
print(f'date_time: {faker.date_time()}')
print(f'date_time_ad: {faker.date_time_ad()}')
print(f'date_time_between: {faker.date_time_between()}')
print(f'date_time_between_dates: {faker.date_time_between_dates()}')
print(f'date_time_this_century: {faker.date_time_this_century()}')
print(f'date_time_this_decade: {faker.date_time_this_decade()}')
print(f'date_time_this_month: {faker.date_time_this_month()}')
print(f'date_time_this_year: {faker.date_time_this_year()}')
print(f'day_of_month: {faker.day_of_month()}')
print(f'day_of_week: {faker.day_of_week()}')
print(f'domain_name: {faker.domain_name()}')
print(f'domain_word: {faker.domain_word()}')
print(f'ean: {faker.ean13()}')
print(f'ean8: {faker.ean8()}')
print(f'ein: {faker.ein()}')
print(f'email: {faker.email()}')
print(f'file_extension: {faker.file_extension()}')
print(f'file_name: {faker.file_name()}')
print(f'file_path: {faker.file_path()}')
print(f'firefox: {faker.firefox()}')
print(f'first_name: {faker.first_name()}')
print(f'first_name_female: {faker.first_name_female()}')
print(f'first_name_male: {faker.first_name_male()}')
#print(f'format: {faker.format()}')
print(f'free_email: {faker.free_email()}')
print(f'free_email_domain: {faker.free_email_domain()}')
print(f'future_date: {faker.future_date()}')
print(f'future_datetime: {faker.future_datetime()}')
#print(f'get_formatter: {faker.get_formatter()}')
print(f'get_providers: {faker.get_providers()}')
print(f'hex_color: {faker.hex_color()}')
print(f'hexify: {faker.hexify()}')
print(f'hostname: {faker.hostname()}')
print(f'iban: {faker.iban()}')
print(f'image_url: {faker.image_url()}')
print(f'internet_explorer: {faker.internet_explorer()}')
print(f'invalid_ssn: {faker.invalid_ssn()}')
print(f'ios_platform_token: {faker.ios_platform_token()}')
print(f'ipv4: {faker.ipv4()}')
print(f'ipv4_network_class: {faker.ipv4_network_class()}')
print(f'ipv4_private: {faker.ipv4_private()}')
print(f'ipv4_public: {faker.ipv4_public()}')
print(f'ipv6: {faker.ipv6()}')
#print(f'isbn10: {faker.ibn10'()}')
#print(f'isbn13: {faker.isbn1'()}')
#print(f'iso8601: {faker.iso801'()}')
print(f'itin: {faker.itin()}')
print(f'job: {faker.job()}')
print(f'language_code:{faker.language_code()}')
print(f'last_name: {faker.last_name()}')
print(f'last_name_female: {faker.last_name_female()}')
print(f'last_name_male: {faker.last_name_male()}')
print(f'latitude: {faker.latitude()}')
print(f'latlng: {faker.latlng()}')
print(f'lexify: {faker.lexify()}')
print(f'license_plate: {faker.license_plate()}')
print(f'linux_platform_token: {faker.linux_platform_token()}')
print(f'linux_processor: {faker.linux_processor()}')
print(f'local_latlng: {faker.local_latlng()}')
print(f'locale: {faker.locale()}')
print(f'location_on_land: {faker.location_on_land()}')
print(f'longitude: {faker.longitude()}')
print(f'mac_address: {faker.mac_address()}')
print(f'mac_platform_token: {faker.mac_platform_token()}')
print(f'mac_processor: {faker.mac_processor()}')
print(f'md5: {faker.md5()}')
print(f'military_apo: {faker.military_apo()}')
print(f'military_dpo: {faker.military_dpo()}')
print(f'military_ship: {faker.military_ship()}')
print(f'military_state: {faker.military_state()}')
print(f'mime_type: {faker.mime_type()}')
print(f'month: {faker.month()}')
print(f'month_name: {faker.month_name()}')
print(f'msisdn: {faker.msisdn()}')
print(f'name: {faker.name()}')
print(f'fname_female: {faker.name_female()}')
print(f'name_male: {faker.name_male()}')
print(f'null_boolean: {faker.null_boolean()}')
print(f'numerify: {faker.numerify()}')
print(f'opera: {faker.opera()}')
print(f'paragraph: {faker.paragraph()}')
print(f'paragraphs: {faker.paragraphs()}')
#print(f'parse: {faker.parse()}')
print(f'password: {faker.password()}')
print(f'past_date: {faker.past_date()}')
print(f'past_datetime: {faker.past_datetime()}')
print(f'phone_number: {faker.phone_number()}')
print(f'postalcode: {faker.postalcode()}')
print(f'postalcode_in_state: {faker.postalcode_in_state()}')
print(f'postalcode_plus4: {faker.postalcode_plus4()}')
print(f'postcode: {faker.postcode()}')
print(f'postcode_in_state: {faker.postcode_in_state()}')
print(f'prefix: {faker.prefix()}')
print(f'prefix_female: {faker.prefix_female()}')
print(f'prefix_male: {faker.prefix_male()}')
print(f'profile: {faker.profile()}')
#print(f'provider: {faker.provider()}')
#print(f'providers: {faker.providers()}')
print(f'pybool: {faker.pybool()}')
print(f'pydecimal: {faker.pydecimal()}')
print(f'pydict: {faker.pydict()}')
print(f'pyfloat: {faker.pyfloat()}')
print(f'pyint: {faker.pyint()}')
print(f'pyiterable: {faker.pyiterable()}')
print(f'pylist: {faker.pylist()}')
print(f'pyset: {faker.pyset()}')
print(f'pystr: {faker.pystr()}')
print(f'pystr_format: {faker.pystr_format()}')
print(f'pystruct: {faker.pystruct()}')
print(f'pytuple: {faker.pytuple()}')
#print(f'random: {faker.random()}')
print(f'random_choices: {faker.random_choices()}')
print(f'random_digit: {faker.random_digit()}')
print(f'random_digit_not_null: {faker.random_digit_not_null()}')
print(f'random_digit_not_null_or_empty: {faker.random_digit_not_null_or_empty()}')
print(f'random_digit_or_empty: {faker.random_digit_or_empty()}')
print(f'random_element: {faker.random_element()}')
print(f'random_elements: {faker.random_elements()}')
print(f'random_int: {faker.random_int()}')
print(f'random_letter: {faker.random_letter()}')
print(f'random_letters: {faker.random_letters()}')
print(f'random_lowercase_letter: {faker.random_lowercase_letter()}')
print(f'random_number: {faker.random_number()}')
print(f'random_sample: {faker.random_sample()}')
print(f'random_uppercase_letter: {faker.random_uppercase_letter()}')
print(f'randomize_nb_elements: {faker.randomize_nb_elements()}')
print(f'rgb_color: {faker.rgb_color()}')
print(f'rgb_css_color: {faker.rgb_css_color()}')
print(f'safari: {faker.safari()}')
print(f'safe_color_name: {faker.safe_color_name()}')
print(f'safe_email: {faker.safe_email()}')
print(f'safe_hex_color: {faker.safe_hex_color()}')
print(f'secondary_address: {faker.secondary_address()}')
print(f'seed: {faker.seed()}')
print(f'seed_instance: {faker.seed_instance()}')
print(f'sentence: {faker.sentence()}')
print(f'sentences: {faker.sentences()}')
#print(f'set_formatter: {faker.set_formatter()}')
print(f'sha1: {faker.sha1()}')
print(f'sha256: {faker.sha256()}')
print(f'simple_profile: {faker.simple_profile()}')
print(f'slug: {faker.slug()}')
print(f'ssn: {faker.ssn()}')
print(f'state: {faker.state()}')
#print(f'state_abbr: {fakerstate_abbr()}')
print(f'street_address: {faker.street_address()}')
print(f'street_name: {faker.street_name()}')
print(f'street_suffix: {faker.street_suffix()}')
print(f'suffix: {faker.suffix()}')
print(f'suffix_female: {faker.suffix_female()}')
print(f'suffix_male: {faker.suffix_male()}')
print(f'text: {faker.text()}')
print(f'texts: {faker.texts()}')
print(f'time: {faker.time()}')
print(f'time_delta: {faker.time_delta()}')
print(f'time_object: {faker.time_object()}')
print(f'time_series: {faker.time_series()}')
print(f'timezone: {faker.timezone()}')
print(f'tld: {faker.tld()}')
print(f'unix_device: {faker.unix_device()}')
print(f'unix_partition: {faker.unix_partition()}')
print(f'unix_time: {faker.unix_time()}')
print(f'upc_a: {faker.upc_a()}')
print(f'upc_e: {faker.upc_e()}')
print(f'uri: {faker.uri()}')
print(f'uri_extension: {faker.uri_extension()}')
print(f'uri_page: {faker.uri_page()}')
print(f'uri_path: {faker.uri_path()}')
print(f'url: {faker.url()}')
print(f'user_agent: {faker.user_agent()}')
print(f'user_name: {faker.user_name()}')
print(f'uuid4: {faker.uuid4()}')
print(f'windows_platform_token: {faker.windows_platform_token()}')
print(f'word: {faker.word()}')
print(f'words: {faker.words()}')
print(f'year: {faker.year()}')
print(f'zipcode: {faker.zipcode()}')
print(f'zipcode_in_state: {faker.zipcode_in_state()}')
print(f'zipcode_plus4: {faker.zipcode_plus4()}')
