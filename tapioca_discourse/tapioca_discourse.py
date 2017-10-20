# coding: utf-8

from tapioca import (JSONAdapterMixin, TapiocaAdapter,
                     generate_wrapper_from_adapter)

from .resource_mapping import RESOURCE_MAPPING


class DiscourseClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://try.discourse.org'
    resource_mapping = RESOURCE_MAPPING

    def get_api_root(self, api_params):
        api_root = api_params.get('api_root')

        if api_root:
            return api_root
        else:
            return self.api_root

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(DiscourseClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        auth = {
            'api_key': api_params.get('api_key'),
            'api_username': api_params.get('api_username'),
        }

        if 'params' in params:
            params['params'].update(auth)
        else:
            params['params'] = auth

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


Discourse = generate_wrapper_from_adapter(DiscourseClientAdapter)
