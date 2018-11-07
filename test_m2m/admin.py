from django.contrib import admin
from .models import ExpGroup, ExpName, Line, Location, EcoCharacter, FieldCharacter

# Register your models here.


class LineAdmin(admin.ModelAdmin):
    list_display = ('line_name', 'line_institute', 'line_owner', 'line_contactor', 'line_type',
                    'line_parents', 'line_target_date', 'line_phone', 'line_email', 'test_year',
                    'test_group', 'test_name')


class ExpGroupAdmin(admin.ModelAdmin):
    list_display = ('test_group',)


class ExpNameAdmin(admin.ModelAdmin):
    list_display = ('test_group', 'test_name')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('test_unit', 'testPoint_name', 'testPoint_loc', 'testLoc_longitude', 'testLoc_latitude',
                    'testLoc_altitude', 'address', 'contacts', 'contact_num', 'contact_email')
    filter_horizontal = ('test_group', 'test_name')


class EcoCharacterAdmin(admin.ModelAdmin):
    list_display = ('line_name', 'pod_high', 'weight_HGrain', 'rate_PurpleSpot', 'rate_BrownSpot',
                    'rate_Insect', 'rate_others', 'remarks')


class FieldCharacterAdmin(admin.ModelAdmin):
    list_display = ('line_name', 'seeding_date', 'seeding_state', 'flowering_period',
                    'mature_period', 'harvest_period', 'No_GrowDays', 'leaf_shape',
                    'flower_color', 'hairy_color', 'pod_BearHabit', 'plant_architecture',
                    'pod_dehiscence', 'deciduous', 'lodging', 'root_rot', 'smv',
                    'in_green', 'virus_other')


admin.site.register(Line, LineAdmin)
admin.site.register(ExpGroup, ExpGroupAdmin)
admin.site.register(ExpName, ExpNameAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(EcoCharacter, EcoCharacterAdmin)
admin.site.register(FieldCharacter, FieldCharacterAdmin)
