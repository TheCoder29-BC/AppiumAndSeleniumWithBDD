# This is a Feature file

@webpage #with @ you create an Tag
Feature: SocialNetwork Webpage Tests

    @profile @login @logout
    Scenario: Profile related cases

        Given Launch the profile page
        When Change profile pic
        Then Verify profile pic

    @feed @login
    Scenario: Feeds related cases

        Given Launch the feed page
        When publish the feed
        Then Verify feed


    @pages
    Scenario: Pages related cases

        Given Launch the page
        When update the page data
        Then Verify page

    @group @profile
    Scenario: Group related cases

        Given Launch the group
        When update the group details
        Then Verify group

"""
Execute in Terminal the script by using tag

    - beave --tags-help
    - behave SocialNetworkSite.feature --tags=tagName or behave SocialNetworkSite.feature --tags tagName

Exectue tags by combinations

To execute scenario or feature file if it as any t1 or t2 tag (,)

    - behave SocialNetworkSite.feature --tags=t1,t2 (run scenarios tagged reg or sanity)

To execute scenario or feature file only if it as both the tags t1 and t2 tag

    -behave SocialNetworkSite.feature --tags=t1 --tags=t2 (run scenarios tagged both reg and sanity)

To exclude or remove specific tag ( - or ~ )

    -behave SocialNetworkSite.feature --tags=-t1 (run everthing except c) ( - or ~ )
"""