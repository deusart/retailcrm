import retailcrm

retailcrm.v5.reference.sites.store_period()

for reference in retailcrm.v5.reference:
    reference.store_period()



# from retailcrm.engine import CrmEngine
# from config import settings
# engine = CrmEngine(settings, '')

# print(settings.API_KEY)
# print(engine.api_key)
# print(urls.reference.sites)
# print(engine.get_response(urls.reference.sites))

# from retailcrm.entitysets import EntitySets
# from retailcrm.engine import CrmEngine
# from retailcrm.debug import Debug
# from retailcrm import crm

# from config import settings

# debug = Debug(settings.OUTPUT)
# entitysets = EntitySets(settings)
# print(entitysets['reference'])

# site = crm.Reference(entitysets['reference']['sites'], debug),