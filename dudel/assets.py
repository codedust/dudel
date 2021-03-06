from dudel import app
from flask_assets import Environment, Bundle
from webassets.filter import get_filter

assets = Environment(app)

# SCSS
scss = Bundle(
    'scss/_vars.scss',
    'scss/main.scss',
    'scss/action.scss',
    'scss/poll.scss',
    'scss/menu.scss',
    'scss/form.scss',
    'scss/calendar.scss',
    'scss/iconpreview.scss',
    'scss/timeinput.scss',
    'scss/slider.scss',
    filters=get_filter('scss', load_paths='.'),
    output='gen/scss.css')
assets.register('scss', scss)

# CSS
css_all = Bundle(
    'css/bootstrap.css',
    'css/font-awesome.css',
    'css/jquery-ui.css',
    'css/jquery-range.css',
    'css/jquery-ui-timepicker-addon.css',
    'css/jquery.colorpicker.css',
    scss,
    output='gen/all.css')
assets.register('css_all', css_all)

# CoffeeScript
coffee = Bundle(
    'coffee/gettext.coffee',
    'coffee/common.coffee',
    'coffee/create.coffee',
    'coffee/datetime.coffee',
    'coffee/dateoffset.coffee',
    'coffee/votefilter.coffee',
    'coffee/vote.coffee',
    'coffee/slug.coffee',
    'coffee/slider.coffee',
    filters='coffeescript',
    output='gen/coffee.js'
)
assets.register('coffee', coffee)

# JavaScript Libraries
js_libs = Bundle(
    'js/lib/jquery.js',
    'js/lib/jquery-ui.min.js',
    'js/lib/jquery-range.min.js',
    'js/lib/bootstrap.js',
    'js/lib/sugar.js',
    'js/lib/sugar-de.js',
    'js/lib/pofile.js',
    # 'js/lib/date-de-DE.js',
    # 'js/lib/date-en-US.js',
    'js/lib/jquery.colorpicker.js',
    'js/lib/moment.min.js',
    'js/lib/mousetrap.min.js',
    output='gen/jslibs.js'
)
assets.register('js_libs', js_libs)

# All javascript + compiled coffescript
js_all = Bundle(
    js_libs,
    coffee,
    'js/util.js',
    'js/main.js',
    'js/custom-select.jquery.js',
    # 'js/poll_edit_choices.js',
    output='gen/app.js'
)
assets.register('js_all', js_all)

