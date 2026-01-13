import type { ConfigType } from '@plone/registry';
import installSettings from './config/settings';
import Libras from '@plonegovbr/volto-vlibras/components/Libras';

function applyConfig(config: ConfigType) {
  installSettings(config);

  config.settings.appExtras = [
    ...config.settings.appExtras,
    {
      match: '',
      component: Libras,
    },
  ];

  return config;
}

export default applyConfig;
