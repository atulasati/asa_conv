from django.contrib import admin

from .models import Mill, Entry, Party, Weight, Item

class MillAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
admin.site.register(Mill, MillAdmin)

class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
admin.site.register(Party, PartyAdmin)

class WeightAdmin(admin.ModelAdmin):
    list_display = ('value',)
admin.site.register(Weight, WeightAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'mill', 'party', 'item', "item_rate", "bags", "weight_per_bag", "_total_weight", "_brokerage_party", "_brokerage_mill")
    def _total_weight(self, obj):
    	total_weight_qtl = (obj.bags * obj.weight_per_bag.value) /100
    	return "%s qtl" % total_weight_qtl
    def _brokerage_party(self, obj):
    	brokerage_party = (obj.bags * obj.party_brokage)
    	return "%s Rs." % brokerage_party
    def _brokerage_mill(self, obj):
    	total_weight_qtl = (obj.bags * obj.weight_per_bag.value) /100
    	return "%s Rs." % (total_weight_qtl*obj.mill_brokage)

admin.site.register(Entry, EntryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('value',)
admin.site.register(Item, ItemAdmin)