<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <Label class="action-bar-title" text="Mea Kanu" horizontalAlignment="center" />
            <ActionItem @tap="openCam" android.systemIcon="picture_frame" android.position="actionBar"/>
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_camera" @tap="openCam"/>
        </ActionBar>
        <RadListView ref="listView" for="plant in plantList" @itemTap="onItemTap" class="list-group">
            <ListViewLinearLayout v-tkListViewLayout scrollDirection="vertical"/>
            <v-template>

                <GridLayout rows="*, *, *" columns="*, *" class="list-group-item-content">
                    <Label :text="plant.name" class="text-primary list-group-item-text font-weight-bold"/>
                    <Label col="1" horizontalAlignment="right" class="list-group-item-text m-r-5"/>

                    <Label row="1" class="hr-dark m-t-5 m-b-5" colSpan="2"/>

                    <Image row="2" :src="plant.picture" stretch="aspectFill" height="120" class="m-r-20" loadMode="async"/>
                    <StackLayout row="2" col="1" verticalAlignment="center" class="list-group-item-text">
                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf0c3;   " class="fa text-primary"/>
                                <Span :text="plant.label"/>
                            </FormattedString>
                        </Label>

                        <Label class="p-b-10">
                            <Span text.decode="&#xf12a;   " class="fa text-primary"/>
                            <Span :text="plant.scientificName"/>
                        </Label>

                        <Label class="p-b-10">
                            <Span text.decode="&#xf085;   " class="fa text-primary"/>
                            <Span :text="plant.hawaiianName"/>
                        </Label>
                    </StackLayout>
                </GridLayout>

                <!--<StackLayout orientation="vertical">-->
                <!--<Label :text="plant.name"></Label>-->
                <!--<Image :src="plant.picture" class="list-picture"/>--
            <!--</StackLayout>-->
            </v-template>

        </RadListView>
    </Page>
</template>

<script>

    import * as camera from "nativescript-camera";
    import axios from 'axios';
    export default {

        data() {
            return {
                picture: null,
                plantList: [
                    {name: "Acalypha Hispida", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'invasive', picture: "~/images/Acalypha_hispida.jpg"},
                    {name: "Alocasia Macrorrhiza", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'endangered', picture: "~/images/Alocasia_macrorrhiza.jpg"},
                    {name: "Aloe Vera", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'invasive', picture: "~/images/Aloe_vera.jpg"},
                    {name: "Alpinia Purpurata", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'endangered', picture: "~/images/Alpinia_purpurata.jpg"},
                    {name: "Anthurium Andreanum", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'endangered', picture: "~/images/Anthurium_andreanum.jpg"},
                    {name: "Azadirachta Indica", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'invasive', picture: "~/images/Azadirachta_indica.jpg"},
                    {name: "Bauhinia Variegata", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'endangered', picture: "~/images/Bauhinia_variegata.jpg"},
                    {name: "Bixa Orellana", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'invasive', picture: "~/images/Bixa_orellana.jpg"},
                    {name: "Blighia Sapida", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'endangered', picture: "~/images/Blighia_sapida.jpg"},
                    {name: "Bombax Glabra", scientificName: 'placeholder', hawaiianName: 'hawaii placeholder', label: 'invasive', picture: "~/images/Bombax_glabra.jpg"},
                ]
            }
        },
        methods: {
            openCam() {
                let imageModule = require('ui/image');
                camera.requestPermissions();

                        camera.takePicture({width:300, height:300, keepAspectRatio: true, saveToGallery: true})
                            .then(function (imageAsset){
                                console.log("Result is an image asset instance");
                                let image = new imageModule.Image();
                                image.src = imageAsset;
                                axios.post('https://mea-kanu.firebaseio.com/data.json', image.src)
                                    .then(response => {
                                        console.log(response);
                                    }, error => {
                                        console.log(error);
                                    })
                            }).catch(function (err) {
                            console.log("Error -> " + err.message);
                        });

            },
            uploadPic() {

            },
            goBack() {
                console.log('testing goBack function is this getting updated');
            },
            sendPicture() {
                console.log('this should appear');
            },
            onItemTap() {

            }

        },
        // created() {
        //
        // let imageModule = require('ui/image');
        // camera.takePicture({width:300, height:300, saveToGallery: true})
        //     .then(function (imageAsset){
        //         console.log("Result is an image asset instance");
        //         let image = new imageModule.Image();
        //         image.src = imageAsset;
        //     }).catch(function (err) {
        //         console.log("Error -> " + err.message);
        // });
        // }
    }
</script>

<style scoped lang="scss">
    @import '../app-variables';
    // End custom common variables

    // Custom styles
    .list-picture{
        height: 100;
        width: 100;
    }

    .list-group {
        .list-group-item-content {
            padding: 8 15 4 15;
            background-color: $background-light;
        }

        .list-group-item-text {
            margin: 2 3;
        }

        .fa {
            color: $accent-dark;
        }
    }
    .back{
        background-color: gray;
    }
</style>

        <!--<RadListView v-if="!isLoading" for="item in carList" @itemTap="onItemTap" class="list-group">-->
            <!--<ListViewLinearLayout v-tkListViewLayout scrollDirection="Vertical"/>-->
            <!--<v-template>-->
                <!--<GridLayout rows="*, *, *" columns="*, *" class="list-group-item-content">-->
                    <!--<Label :text="item.name" class="text-primary list-group-item-text font-weight-bold"/>-->
                    <!--<Label col="1" horizontalAlignment="right" class="list-group-item-text m-r-5">-->
                        <!--<FormattedString>-->
                            <!--<Span text.decode="&euro;"/>-->
                            <!--<Span :text="item.price"/>-->
                            <!--<Span text="/day"/>-->
                        <!--</FormattedString>-->
                    <!--</Label>-->

                    <!--<Label row="1" class="hr-light m-t-5 m-b-5" colSpan="2"/>-->

                    <!--<Image row="2" :src="item.imageUrl" stretch="aspectFill" height="120" class="m-r-20" loadMode="async"/>-->

                    <!--<StackLayout row="2" col="1" verticalAlignment="center" class="list-group-item-text">-->
                        <!--<Label class="p-b-10">-->
                            <!--<FormattedString ios.fontFamily="system">-->
                                <!--<Span text.decode="&#xf1b9;   " class="fa text-primary"></Span>-->
                                <!--<Span :text="item.class"/>-->
                            <!--</FormattedString>-->
                        <!--</Label>-->
                        <!--<Label class="p-b-10">-->
                            <!--<FormattedString ios.fontFamily="system">-->
                                <!--<Span text.decode="&#xf085;   " class="fa text-primary"/>-->
                                <!--<Span :text="item.transmission"/>-->
                                <!--<Span text=" Transmission"/>-->
                            <!--</FormattedString>-->
                        <!--</Label>-->
                        <!--<Label class="p-b-10">-->
                            <!--<FormattedString ios.fontFamily="system">-->
                                <!--<Span text.decode="&#xf2dc;   " class="fa text-primary"/>-->
                                <!--<Span :text="item.hasAC ? 'Yes' : 'No'"/>-->
                            <!--</FormattedString>-->
                        <!--</Label>-->
                    <!--</StackLayout>-->
                <!--</GridLayout>-->
            <!--</v-template>-->
        <!--</RadListView>-->
        <!--<ActivityIndicator v-else :busy="isLoading"/>-->
    <!--</Page>-->
<!--</template>-->

<!--<script>-->
    <!--import CarDetails from "./CarDetails";-->

    <!--export default {-->
        <!--computed: {-->
            <!--carList() {-->
                <!--return this.$root.cars;-->
            <!--},-->

            <!--isLoading() {-->
                <!--return !this.carList.length;-->
            <!--}-->
        <!--},-->

        <!--methods: {-->
            <!--onItemTap(e) {-->
                <!--this.$emit("select", e.item);-->
                <!--this.$navigateTo(CarDetails, { props: { car: e.item } });-->
            <!--}-->
        <!--}-->
    <!--};-->
<!--</script>-->

<!--<style scoped lang="scss">-->
    <!--// Start custom common variables-->
    <!--@import '../app-variables';-->
    <!--// End custom common variables-->

    <!--// Custom styles-->
    <!--.list-group {-->
        <!--.list-group-item-content {-->
            <!--padding: 8 15 4 15;-->
            <!--background-color: $background-light;-->
        <!--}-->

        <!--.list-group-item-text {-->
            <!--margin: 2 3;-->
        <!--}-->

        <!--.fa {-->
            <!--color: $accent-dark;-->
        <!--}-->
    <!--}-->
<!--</style>-->
