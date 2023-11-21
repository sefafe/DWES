package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class GamesData {
    private String name;
    private String imageUrl;

    public GamesData(JSONObject json){
        try {
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
        }catch (JSONException e){
            e.printStackTrace();
        }
    }

    public String getName(){
        return name;
    }

    public String getImageUrl() {
        return imageUrl;
    }
}
