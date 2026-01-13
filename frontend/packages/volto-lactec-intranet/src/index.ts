import type { ConfigType } from '@plone/registry';
import installSettings from './config/settings';
import Libras from '@plonegovbr/volto-vlibras/components/Libras';
import installViews from './config/views';

function applyConfig(config: ConfigType) {
  installSettings(config);
  installViews(config);

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
